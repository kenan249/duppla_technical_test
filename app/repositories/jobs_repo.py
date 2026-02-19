from uuid import UUID
from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models import Job as JobModel
from app.domain.models.job import Job
from app.domain.enums.job_status import JobStatus
from app.db.engine import AsyncSessionLocal


class JobsRepository:
    def __init__(self):
        self.session = AsyncSessionLocal()

    def _to_domain(self, model: JobModel) -> Job:
        return Job(
            id=model.id,
            status=JobStatus(model.status),
            total=model.total,
            processed=model.processed,
            requested_ids=model.requested_ids,
            error=model.error,
            created_at=model.created_at,
            updated_at=model.updated_at
        )

    def _to_model(self, job: Job) -> JobModel:
        return JobModel(
            id=job.id,
            status=job.status.value,
            total=job.total,
            processed=job.processed,
            requested_ids=job.requested_ids,
            error=job.error,
            created_at=job.created_at,
            updated_at=job.updated_at
        )

    async def create(self, job: Job) -> Job:
        model = self._to_model(job)
        self.session.add(model)
        await self.session.commit()
        await self.session.refresh(model)
        return self._to_domain(model)

    async def get_by_id(self, job_id: UUID) -> Optional[Job]:
        query = select(JobModel).where(JobModel.id == job_id)
        result = await self.session.execute(query)
        model = result.scalar_one_or_none()
        if model is None:
            return None
        return self._to_domain(model)

    async def update(self, job: Job) -> Job:
        query = select(JobModel).where(JobModel.id == job.id)
        result = await self.session.execute(query)
        model = result.scalar_one_or_none()
        if model is None:
            raise ValueError(f"Job {job.id} not found")
        
        model.status = job.status.value
        model.total = job.total
        model.processed = job.processed
        model.requested_ids = job.requested_ids
        model.error = job.error
        
        await self.session.commit()
        await self.session.refresh(model)
        return self._to_domain(model)