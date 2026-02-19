from uuid import UUID
from typing import Optional
from decimal import Decimal

from fastapi import APIRouter, Query, status

from app.api.schemas.documents import (
    DocumentCreate,
    DocumentUpdate,
    DocumentStatusUpdate,
    DocumentResponse,
    DocumentListResponse,
)
from app.services.documents_service import DocumentsService
from app.repositories.documents_repo import DocumentsRepository, DocumentFilters
from app.domain.enums.document_status import DocumentStatus


class DocumentsController:
    def __init__(self):
        self.service = DocumentsService()
        self.router = APIRouter(prefix="/documents", tags=["documents"])
        
        self.router.add_api_route("", self.create, methods=["POST"], response_model=DocumentResponse, status_code=status.HTTP_201_CREATED)
        self.router.add_api_route("", self.list, methods=["GET"], response_model=DocumentListResponse)
        self.router.add_api_route("/{document_id}", self.get, methods=["GET"], response_model=DocumentResponse)
        self.router.add_api_route("/{document_id}", self.update, methods=["PATCH"], response_model=DocumentResponse)
        self.router.add_api_route("/{document_id}", self.delete, methods=["DELETE"], status_code=status.HTTP_204_NO_CONTENT)
        self.router.add_api_route("/{document_id}/status", self.change_status, methods=["PATCH"], response_model=DocumentResponse)

    async def create(self, body: DocumentCreate):
        document = await self.service.create_document(
            document_type=body.document_type,
            amount=body.amount,
            metadata=body.metadata,
        )
        return self._to_response(document)

    async def get(self, document_id: UUID):
        document = await self.service.get_document(document_id)
        return self._to_response(document)

    async def update(self, document_id: UUID, body: DocumentUpdate):
        document = await self.service.update_document(
            document_id=document_id,
            document_type=body.document_type,
            amount=body.amount,
            metadata=body.metadata,
        )
        return self._to_response(document)

    async def delete(self, document_id: UUID):
        await self.service.delete_document(document_id)

    async def list(
        self,
        document_type: Optional[str] = Query(None),
        status: Optional[DocumentStatus] = Query(None),
        amount_min: Optional[Decimal] = Query(None),
        amount_max: Optional[Decimal] = Query(None),
        page: int = Query(1, ge=1),
        page_size: int = Query(10, ge=1, le=100),
    ):
        filters = DocumentFilters(
            document_type=document_type,
            status=status,
            min_amount=amount_min,
            max_amount=amount_max,
        )
        page_result = await self.service.list_documents(filters, page, page_size)
        return DocumentListResponse(
            items=[self._to_response(doc) for doc in page_result.items],
            total=page_result.total,
            page=page_result.page,
            page_size=page_result.page_size,
        )

    async def change_status(self, document_id: UUID, body: DocumentStatusUpdate):
        document = await self.service.change_status(document_id, body.status)
        return self._to_response(document)

    def _to_response(self, document) -> DocumentResponse:
        return DocumentResponse(
            id=document.id,
            document_type=document.type,
            amount=document.amount,
            status=document.status,
            created_at=document.created_at,
            metadata=document.metadata,
        )


router = DocumentsController().router