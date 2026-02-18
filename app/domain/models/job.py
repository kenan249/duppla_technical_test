from dataclasses import dataclass, replace
from datetime import datetime
from uuid import UUID
from typing import List, Optional

from app.domain.enums.job_status import JobStatus
from app.domain.enums.business_error_code import BusinessErrorCode as business_error_code
from app.domain.errors import ValidationError


@dataclass
class Job:
    id: UUID
    status: JobStatus
    total: int
    processed: int
    requested_ids: List[str]
    error: Optional[str]
    created_at: datetime
    updated_at: datetime

    def mark_queued(self, total: int, requested_ids: List[str]) -> "Job":
        return replace(
            self,
            status=JobStatus.QUEUED,
            total=total,
            processed=0,
            requested_ids=requested_ids,
            error=None,
        )

    def mark_running(self) -> "Job":
        if self.status != JobStatus.QUEUED:
            raise ValidationError(business_error_code=business_error_code.JOB_002)
        return replace(self, status=JobStatus.RUNNING)

    def update_progress(self, processed: int) -> "Job":
        if processed < 0 or processed > self.total:
            raise ValidationError(business_error_code=business_error_code.JOB_004)
        return replace(self, processed=processed)

    def mark_completed(self) -> "Job":
        return replace(
            self,
            status=JobStatus.COMPLETED,
            processed=self.total,
            error=None,
        )

    def mark_failed(self, error: str) -> "Job":
        return replace(
            self,
            status=JobStatus.FAILED,
            error=error,
        )

    def is_finished(self) -> bool:
        return self.status in (JobStatus.COMPLETED, JobStatus.FAILED)