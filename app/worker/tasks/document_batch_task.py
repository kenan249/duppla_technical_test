import asyncio
from typing import List
from fastapi import logger
from app.domain.errors import ValidationError
from app.worker.helpers.batch_input_validator import BatchInputValidator
from app.worker.processors.process_document_batch import DocumentBatchProcessor

def process_document_batch(job_id: str, document_ids: List[str], target_status: str) -> None:
    processor = DocumentBatchProcessor()
    try:
        job_uuid, target_status_enum = BatchInputValidator.validate(job_id, document_ids, target_status)
    except ValidationError as e:
        logger.error(f"Invalid input for batch task: {getattr(e, 'message', str(e))}")
        return                          

    asyncio.run(
        processor.run(
            job_uuid=job_uuid,
            document_ids=document_ids,
            target_status=target_status,
            target_status_enum=target_status_enum,
            )
        )