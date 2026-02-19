from __future__ import annotations

from rq import Queue
from app.infra.redis_client import RedisClient
from app.infra.settings import DOCUMENT_BATCH_QUEUE_NAME


class BatchDocumentQueueAdapter:
    def __init__(self):
        self.redis_conn = RedisClient().get_redis_sync()
        self.queue = Queue(DOCUMENT_BATCH_QUEUE_NAME, connection=self.redis_conn)

    def enqueue(self, job_id: str, documents_id: list[str], target_status: str) -> str:
        payload = {
            "job_id": job_id,
            "documents_id": documents_id,
            "target_status": target_status,
        }
        rq_job = self.queue.enqueue("app.worker.tasks.process_batch.process_document_batch", payload)
        return rq_job.id
