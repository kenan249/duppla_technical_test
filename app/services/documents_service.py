from uuid import UUID, uuid4
from datetime import datetime,timezone
from decimal import Decimal
from typing import Optional, List

from app.repositories.documents_repo import DocumentsRepository, DocumentFilters
from app.domain.models.document import Document
from app.domain.models.page import Page
from app.domain.models.batch_result import BatchResult
from app.domain.enums.document_status import DocumentStatus
from app.domain.errors import NotFoundError, ValidationError


class DocumentsService:
    def __init__(self):
        self.documents_repo = DocumentsRepository()

    async def create_document(
        self,
        document_type: str,
        amount: Decimal,
        metadata: Optional[dict] = None,
    ) -> Document:
        now = datetime.now(timezone.utc)
        document = Document(
            id=uuid4(),
            type=document_type,
            amount=amount,
            status=DocumentStatus.DRAFT,
            created_at=now,
            metadata=metadata or {},
        )
        return await self.documents_repo.create(document)

    async def get_document(self, document_id: UUID) -> Document:
        document = await self.documents_repo.get_by_id(document_id)
        if document is None:
            raise NotFoundError(
                message=f"Document {document_id} not found",
                code="DOCUMENT_NOT_FOUND"
            )
        return document

    async def update_document(
        self,
        document_id: UUID,
        document_type: Optional[str] = None,
        amount: Optional[Decimal] = None,
        metadata: Optional[dict] = None,
    ) -> Document:
        document = await self.get_document(document_id)
        document = document.update_details(
            document_type=document_type,
            amount=amount,
            metadata=metadata,
        )
        return await self.documents_repo.update(document)

    async def delete_document(self, document_id: UUID) -> None:
        await self.get_document(document_id)
        await self.documents_repo.delete(document_id)

    async def list_documents(
        self,
        filters: DocumentFilters,
        page: int = 1,
        page_size: int = 10,
    ) -> Page[Document]:
        return await self.documents_repo.page(filters, page, page_size)

    async def change_status(
        self,
        document_id: UUID,
        new_status: DocumentStatus,
    ) -> Document:
        document = await self.get_document(document_id)
        document = document.change_status(new_status)
        return await self.documents_repo.update(document)

    async def change_status_bulk(
        self,
        document_ids: List[UUID],
        new_status: DocumentStatus,
    ) -> BatchResult:
        updated = 0
        failed = 0
        errors = []

        for doc_id in document_ids:
            try:
                await self.change_status(doc_id, new_status)
                updated += 1
            except (NotFoundError, ValidationError) as e:
                failed += 1
                errors.append({
                    "document_id": str(doc_id),
                    "error": e.message,
                    "code": e.code,
                })

        return BatchResult(
            total=len(document_ids),
            updated=updated,
            failed=failed,
            errors=errors,
        )
