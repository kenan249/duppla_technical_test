from dataclasses import dataclass
from uuid import UUID
from typing import Optional

from sqlalchemy import select, func
from app.db.engine import AsyncSessionLocal

from app.db.models import Document as DocumentModel
from app.domain.models.document import Document
from app.domain.models.page import Page
from app.domain.enums.document_status import DocumentStatus


@dataclass
class DocumentFilters:
    document_type: Optional[str] = None
    status: Optional[DocumentStatus] = None
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None


class DocumentsRepository:
    def __init__(self):
        self.session = AsyncSessionLocal()

    def _to_domain(self, model: DocumentModel) -> Document:
        # Convierte el status de la BD (minúsculas) al Enum Python (mayúsculas)
        return Document(
            id=model.id,
            type=model.document_type,
            amount=model.amount,
            status=DocumentStatus(model.status),
            created_at=model.created_at,
            metadata=model.metadata_dic or {},
        )

    def _to_model(self, document: Document) -> DocumentModel:
        # Guarda el status en minúsculas en la BD
        return DocumentModel(
            id=document.id,
            document_type=document.type,
            amount=document.amount,
            status=document.status,
            created_at=document.created_at,
            metadata_dic=document.metadata,
        )

    async def create(self, document: Document) -> Document:
        model = self._to_model(document)
        self.session.add(model)
        await self.session.flush()
        await self.session.refresh(model)
        await self.session.commit()
        return self._to_domain(model)

    async def get_by_id(self, document_id: UUID) -> Optional[Document]:
        stmt = select(DocumentModel).where(DocumentModel.id == document_id)
        result = await self.session.execute(stmt)
        model = result.scalar_one_or_none()
        return self._to_domain(model) if model else None

    async def update(self, document: Document) -> Document:
        stmt = select(DocumentModel).where(DocumentModel.id == document.id)
        result = await self.session.execute(stmt)
        model = result.scalar_one_or_none()
        if not model:
            raise ValueError(f"Document {document.id} not found")
        
        model.document_type = document.type
        model.amount = document.amount
        model.status = document.status
        model.metadata = document.metadata
        
        await self.session.flush()
        await self.session.refresh(model)
        await self.session.commit()
        return self._to_domain(model)

    async def delete(self, document_id: UUID) -> None:
        stmt = select(DocumentModel).where(DocumentModel.id == document_id)
        result = await self.session.execute(stmt)
        model = result.scalar_one_or_none()
        if model:
            await self.session.delete(model)
            await self.session.flush()
            await self.session.commit()

    async def page(
        self, filters: DocumentFilters, page: int = 1, page_size: int = 10
    ) -> Page[Document]:
        stmt = select(DocumentModel)
        count_stmt = select(func.count()).select_from(DocumentModel)

        if filters.document_type:
            stmt = stmt.where(DocumentModel.document_type == filters.document_type)
            count_stmt = count_stmt.where(DocumentModel.document_type == filters.document_type)
        if filters.status:
            stmt = stmt.where(DocumentModel.status == filters.status.value)
            count_stmt = count_stmt.where(DocumentModel.status == filters.status.value)
        if filters.min_amount is not None:
            stmt = stmt.where(DocumentModel.amount >= filters.min_amount)
            count_stmt = count_stmt.where(DocumentModel.amount >= filters.min_amount)
        if filters.max_amount is not None:
            stmt = stmt.where(DocumentModel.amount <= filters.max_amount)
            count_stmt = count_stmt.where(DocumentModel.amount <= filters.max_amount)

        total_result = await self.session.execute(count_stmt)
        total = total_result.scalar() or 0

        offset = (page - 1) * page_size
        stmt = stmt.order_by(DocumentModel.created_at.desc()).offset(offset).limit(page_size)

        result = await self.session.execute(stmt)
        models = result.scalars().all()

        return Page(
            items=[self._to_domain(m) for m in models],
            total=total,
            page=page,
            page_size=page_size,
        )

