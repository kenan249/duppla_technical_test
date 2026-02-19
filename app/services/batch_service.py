import logging
from app.domain.enums.document_status import DocumentStatus
from app.infra.batch_document_queue_adapter import BatchDocumentQueueAdapter
from app.services.jobs_service import JobsService
from app.domain.models.job import Job
from app.domain.enums.job_status import JobStatus

logger = logging.getLogger(__name__)
class BatchService:
    def __init__(self):
        self.batch_queue_adapter = BatchDocumentQueueAdapter()
        self.jobs_service = JobsService()

    async def process_batch(self, document_ids: list[str], target_status: DocumentStatus) -> str:
        job= await self.jobs_service.create_job(document_ids)
        logger.info(job)
        self.batch_queue_adapter.enqueue(str(job.id), document_ids, target_status.value)
        return str(job.id)