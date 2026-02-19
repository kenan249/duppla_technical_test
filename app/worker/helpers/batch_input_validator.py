
from typing import Tuple
from uuid import UUID
from pydantic import ValidationError

from app.domain.enums.document_status import DocumentStatus


class BatchInputValidator:

    @classmethod
    def validate(cls, job_id: str, document_ids: list[str], target_status: str) -> Tuple[UUID, DocumentStatus]:
        if not job_id or not isinstance(job_id, str):
            raise ValidationError(message="job_id must be a non-empty string")

        try:
            job_uuid = UUID(job_id)
        except ValueError:
            raise ValidationError(message="job_id must be a valid UUID")

        if not isinstance(document_ids, list) or len(document_ids) == 0:
            raise ValidationError(message="document_ids must be a non-empty list")

        try:
            status_enum = DocumentStatus(target_status)
        except ValueError:
            raise ValidationError(message=f"Invalid target_status: {target_status}")

        return job_uuid, status_enum