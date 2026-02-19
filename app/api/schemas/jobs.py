from uuid import UUID
from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel

from app.domain.enums.job_status import JobStatus


class JobResponse(BaseModel):
    id: UUID
    status: JobStatus
    total: int
    processed: int
    requested_ids: List[str]
    error: Optional[str]
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True