import json
from typing import Any
from app.infra.redis_client import RedisClient

class PublisherJobAdapter:

    def __init__(self):
        self.redis = RedisClient().get_redis_sync()

    def job_channel(self, job_id: str) -> str:
        return f"job:{job_id}"


    def publish_job_event(self, job_id: str, payload: dict[str, Any]) -> None:
        channel = self.job_channel(job_id)
        payload.setdefault("job_id", job_id)
        self.redis.publish(channel, json.dumps(payload))
