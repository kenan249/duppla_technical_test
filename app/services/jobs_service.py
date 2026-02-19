from uuid import UUID, uuid4
from datetime import datetime, timezone
from typing import List, Optional

from app.repositories.jobs_repo import JobsRepository
from app.domain.models.job import Job
from app.domain.enums.job_status import JobStatus
from app.domain.errors import NotFoundError


class JobsService:
    def __init__(self):
        self.jobs_repo = JobsRepository()

    async def create_job(self, document_ids: List[str]) -> Job:
        now = datetime.now(timezone.utc)
        job = Job(
            id=uuid4(),
            status=JobStatus.QUEUED,
            total=len(document_ids),
            processed=0,
            requested_ids=document_ids,
            error=None,
            created_at=now,
            updated_at=now,
        )
        return await self.jobs_repo.create(job)

    async def get_job(self, job_id: UUID) -> Job:
        job = await self.jobs_repo.get_by_id(job_id)
        if job is None:
            raise NotFoundError(
                message=f"Job {job_id} not found",
                code="JOB_NOT_FOUND"
            )
        return job

    async def mark_running(self, job_id: UUID) -> Job:
        job = await self.get_job(job_id)
        job = job.mark_running()
        return await self.jobs_repo.update(job)

    async def update_progress(self, job_id: UUID, processed: int) -> Job:
        job = await self.get_job(job_id)
        job = job.update_progress(processed)
        return await self.jobs_repo.update(job)

    async def mark_completed(self, job_id: UUID) -> Job:
        job = await self.get_job(job_id)
        job = job.mark_completed()
        return await self.jobs_repo.update(job)

    async def mark_failed(self, job_id: UUID, error: str) -> Job:
        job = await self.get_job(job_id)
        job = job.mark_failed(error)
        return await self.jobs_repo.update(job)

    async def increment_succeeded(self, job_id: UUID, by: int = 1) -> Job:
        job = await self.get_job(job_id)
        new_processed = min(job.processed + by, job.total)
        job = job.update_progress(new_processed)
        return await self.jobs_repo.update(job)

    async def increment_failed(self, job_id: UUID, by: int = 1) -> Job:
        job = await self.get_job(job_id)
        new_processed = min(job.processed + by, job.total)
        job = job.update_progress(new_processed)
        return await self.jobs_repo.update(job)
