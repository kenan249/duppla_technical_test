from dataclasses import dataclass
from datetime import datetime

@dataclass
class Job:
    id: str
    status: str
    total: int
    processed: int
    requested_ids: list
    error: str
    created_at: datetime
    updated_at: datetime