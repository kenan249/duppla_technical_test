import json

from app.infra.redis_client import RedisClient
from app.worker.events.job_event import JobEvent

class PublisherJobEventAdapter:

    def __init__(self):
        self.redis = RedisClient().get_redis_sync()

    def job_channel(self, job_id: str) -> str:
        return f"job:{job_id}"


    def publish(self, job_id: str, event: JobEvent) -> None:
        channel = self.job_channel(job_id)
        payload = event.to_dict()
        payload.setdefault("job_id", job_id)
        self.redis.publish(channel, json.dumps(payload))
