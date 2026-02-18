from dataclasses import dataclass
from uuid import UUID
from datetime import datetime
from decimal import Decimal

@dataclass
class Document:
    id: UUID
    type: str
    amount: Decimal
    created_at: datetime
    metadata: dict