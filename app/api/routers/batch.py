from fastapi import APIRouter, status

from app.api.schemas.documents import BatchProcessRequest, BatchProcessResponse
from app.domain.enums.document_status import DocumentStatus
from app.services.batch_service import BatchService
from app.domain.errors import ValidationError
from app.domain.enums.business_error_code import BusinessErrorCode as business_error_code


class BatchController:
    def __init__(self):
        self.batch_service = BatchService()
        self.router = APIRouter(prefix="/documents/batch", tags=["batch"])
        
        self.router.add_api_route("/process", self.process, methods=["POST"], response_model=BatchProcessResponse, status_code=status.HTTP_202_ACCEPTED)

    async def process(self, body: BatchProcessRequest):
        document_ids_str = [str(doc_id) for doc_id in body.document_ids]
        try:
            target_status = DocumentStatus(body.target_status)
        except ValueError:
            raise ValidationError(business_error_code=business_error_code.DOC_004)   
        job_id = await self.batch_service.process_batch(
            document_ids=document_ids_str,
            target_status=target_status,
        )
        return BatchProcessResponse(job_id=job_id)


router = BatchController().router