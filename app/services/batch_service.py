from app.infra.batch_document_queue_adapter import BatchDocumentQueueAdapter
from app.services.jobs_service import JobsService
from app.domain.models.job import Job
from app.domain.enums.job_status import JobStatus

import uuid
class BatchService:
    def __init__(self):
        self.batch_queue_adapter = BatchDocumentQueueAdapter()
        self.jobs_service = JobsService()

    def process_batch(self, document_ids: list[str], target_status: JobStatus) -> str:
        job=self.jobs_service.create_job(document_ids)
        self.batch_queue_adapter.enqueue(str(job.id), document_ids, target_status.value)
        return str(job.id)