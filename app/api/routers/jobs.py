from uuid import UUID

from fastapi import APIRouter

from app.api.schemas.jobs import JobResponse
from app.services.jobs_service import JobsService
from app.repositories.jobs_repo import JobsRepository


class JobsController:
    def __init__(self):
        self.service = JobsService()
        self.router = APIRouter(prefix="/jobs", tags=["jobs"])
        
        self.router.add_api_route("/{job_id}", self.get, methods=["GET"], response_model=JobResponse)

    async def get(self, job_id: UUID):
        job = await self.service.get_job(job_id)
        return JobResponse(
            id=job.id,
            status=job.status,
            total=job.total,
            processed=job.processed,
            requested_ids=job.requested_ids,
            error=job.error,
            created_at=job.created_at,
            updated_at=job.updated_at,
        )


router = JobsController().router