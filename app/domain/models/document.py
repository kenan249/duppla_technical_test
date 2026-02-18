from dataclasses import dataclass, replace
from uuid import UUID
from datetime import datetime
from decimal import Decimal
from typing import Optional

from app.domain.enums.document_status import DocumentStatus
from app.domain.enums.business_error_code import BusinessErrorCode as business_error_code
from app.domain.state_machine import can_transition
from app.domain.errors import ValidationError


@dataclass
class Document:
    id: UUID
    type: str
    amount: Decimal
    status: DocumentStatus
    created_at: datetime
    metadata: dict

    def update_details(
        self,
        document_type: Optional[str] = None,
        amount: Optional[Decimal] = None,
        metadata: Optional[dict] = None,
    ) -> "Document":
        return replace(
            self,
            type=document_type if document_type is not None else self.type,
            amount=amount if amount is not None else self.amount,
            metadata=metadata if metadata is not None else self.metadata,
        )

    def can_transition_to(self, new_status: DocumentStatus) -> bool:
        return can_transition(self.status, new_status)

    def change_status(self, new_status: DocumentStatus) -> "Document":
        if not self.can_transition_to(new_status):
            raise ValidationError(business_error_code=business_error_code.DOC_002)
        return replace(self, status=new_status)

    def with_metadata(self, patch: dict) -> "Document":
        merged = {**self.metadata, **patch}
        return replace(self, metadata=merged)