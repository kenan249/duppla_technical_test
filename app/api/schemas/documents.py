from uuid import UUID
from datetime import datetime
from decimal import Decimal
from typing import Optional, List

from pydantic import BaseModel, Field

from app.domain.enums.document_status import DocumentStatus


class DocumentCreate(BaseModel):
    document_type: str
    amount: Decimal = Field(ge=0)
    metadata: Optional[dict] = None


class DocumentUpdate(BaseModel):
    document_type: Optional[str] = None
    amount: Optional[Decimal] = Field(default=None, ge=0)
    metadata: Optional[dict] = None


class DocumentStatusUpdate(BaseModel):
    status: DocumentStatus


class DocumentResponse(BaseModel):
    id: UUID
    document_type: str
    amount: Decimal
    status: DocumentStatus
    created_at: datetime
    metadata: dict

    class Config:
        from_attributes = True


class DocumentListResponse(BaseModel):
    items: List[DocumentResponse]
    total: int
    page: int
    page_size: int


class BatchProcessRequest(BaseModel):
    document_ids: List[UUID]
    target_status: DocumentStatus


class BatchProcessResponse(BaseModel):
    job_id: UUID