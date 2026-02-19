from fastapi import APIRouter, status

from app.api.schemas.documents import BatchProcessRequest, BatchProcessResponse
from app.services.jobs_service import JobsService
from app.repositories.jobs_repo import JobsRepository
from app.infra.batch_document_queue_adapter import BatchDocumentQueueAdapter


class BatchController:
    def __init__(self):
        self.jobs_service = JobsService()
        self.queue_adapter = BatchDocumentQueueAdapter()
        self.router = APIRouter(prefix="/documents/batch", tags=["batch"])
        
        self.router.add_api_route("/process", self.process, methods=["POST"], response_model=BatchProcessResponse, status_code=status.HTTP_202_ACCEPTED)

    async def process(self, body: BatchProcessRequest):
        document_ids_str = [str(doc_id) for doc_id in body.document_ids]
        
        job = await self.jobs_service.create_job(
            document_ids=document_ids_str,
            target_status=body.target_status.value,
        )
        
        self.queue_adapter.enqueue(
            job_id=str(job.id),
            document_ids=document_ids_str,
            target_status=body.target_status,
        )
        
        return BatchProcessResponse(job_id=job.id)


router = BatchController().router