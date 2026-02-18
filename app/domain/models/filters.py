from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import Literal, Optional

from app.domain.enums import DocumentStatus  # draft/pending/approved/rejected

@dataclass(frozen=True)
class DocumentFilters:
    created_from: Optional[datetime] = None
    created_to: Optional[datetime] = None
    document_type: Optional[str] = None
    status: Optional[DocumentStatus] = None
    amount_min: Optional[Decimal] = None
    amount_max: Optional[Decimal] = None

    sort_by: Literal["created_at", "amount"] = "created_at"
    sort_dir: Literal["asc", "desc"] = "desc"
