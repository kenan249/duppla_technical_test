
from dataclasses import dataclass
import logging
from typing import List, Optional, Tuple
from uuid import UUID

from app.domain.enums.document_status import DocumentStatus
from app.domain.enums.job_status import JobStatus
from app.domain.errors import NotFoundError, ValidationError
from app.infra.publisher_job_event import PublisherJobEventAdapter
from app.services.documents_service import DocumentsService
from app.services.jobs_service import JobsService
from app.worker.events.job_event import JobEvent


@dataclass
class BatchCounters:
    processed: int = 0
    succeeded: int = 0
    failed: int = 0

logger = logging.getLogger(__name__)

class DocumentBatchProcessor:
    def __init__(self):
        self.jobs_service = JobsService()
        self.documents_service = DocumentsService()
        self.events = PublisherJobEventAdapter()

    async def run(self, job_uuid: UUID, document_ids: List[str], target_status: str, target_status_enum: DocumentStatus) -> None:
        job_id_str = str(job_uuid)
        try:
            job = await self.jobs_service.get_job(job_uuid)
        except NotFoundError:
            logger.error(f"Job {job_id_str} not found")
            return

        if job.status in (JobStatus.COMPLETED, JobStatus.FAILED):
            logger.info(f"Job {job_id_str} already finished with status {job.status.value}")
            self.events.publish(
                job_id_str,
                JobEvent(
                    status=job.status.value,
                    processed=job.processed,
                    total=job.total,
                    target_status=target_status,
                    message="Job already finished",
                ),
            )
            return

        try:
            job = await self.jobs_service.mark_running(job_uuid)
        except ValidationError as e:
            logger.error(f"Cannot mark job {job_id_str} as running: {getattr(e, 'message', str(e))}")
            return

        total = job.total or len(document_ids)

        self.events.publish(
            job_id_str,
            JobEvent(
                status="running",
                processed=0,
                total=total,
                target_status=target_status,
            ),
        )

        counters = BatchCounters()

        try:
            for doc_id in document_ids:
                result, reason = await self._process_one_document(doc_id, target_status_enum, counters)

                counters.processed += 1
                await self.jobs_service.update_progress(job_uuid, counters.processed)

                self.events.publish(
                    job_id_str,
                    JobEvent(
                        status="running",
                        processed=counters.processed,
                        total=total,
                        target_status=target_status,
                        current_document_id=doc_id,
                        result=result,
                        reason=reason,
                    ),
                )

            await self.jobs_service.mark_completed(job_uuid)

            self.events.publish(
                job_id_str,
                JobEvent(
                    status="completed",
                    processed=counters.processed,
                    total=total,
                    target_status=target_status,
                    succeeded=counters.succeeded,
                    failed=counters.failed,
                ),
            )

            logger.info(
                f"Job {job_id_str} completed: {counters.succeeded} succeeded, {counters.failed} failed"
            )

        except Exception as e:
            # 6) Systemic error: mark failed and publish failed
            error_message = f"Systemic error: {str(e)}"
            logger.exception(error_message)

            try:
                await self.jobs_service.mark_failed(job_uuid, error_message)
            except Exception:
                logger.exception(f"Failed to mark job {job_id_str} as failed")

            self.events.publish(
                job_id_str,
                JobEvent(
                    status="failed",
                    processed=counters.processed,
                    total=total,
                    target_status=target_status,
                    error=error_message,
                ),
            )

    async def _process_one_document(
        self,
        document_id: str,
        target_status_enum: DocumentStatus,
        counters: BatchCounters,
    ) -> Tuple[str, Optional[str]]:
   
        try:
            doc_uuid = UUID(document_id)
        except ValueError:
            counters.failed += 1
            reason = f"Invalid document_id UUID: {document_id}"
            logger.warning(reason)
            return "failed", reason

        try:
            await self.documents_service.change_status(doc_uuid, target_status_enum)
            counters.succeeded += 1
            return "updated", None

        except NotFoundError:
            counters.failed += 1
            reason = f"Document not found: {document_id}"
            logger.warning(reason)
            return "failed", reason

        except ValidationError as e:
            counters.failed += 1
            reason = f"Invalid transition: {getattr(e, 'message', str(e))}"
            logger.warning(reason)
            return "failed", reason

        except Exception as e:
            counters.failed += 1
            reason = f"Unexpected error: {str(e)}"
            logger.exception(reason)
            return "failed", reason