import redis
import redis.asyncio as redis_async
from dotenv import load_dotenv
import os

class RedisClient:

    def __init__(self):
        load_dotenv()
        self.REDIS_URL = os.getenv("REDIS_URL")

    def get_redis_sync(self) -> redis.Redis:
        return redis.Redis.from_url(
            self.REDIS_URL,
            decode_responses=True,
        )
    
    def get_redis_rq_sync(self) -> redis.Redis:
        return redis.Redis.from_url(
            self.REDIS_URL,
            decode_responses=False,
        )


    def get_redis_async(self) -> redis_async.Redis:
        return redis_async.Redis.from_url(
            self.REDIS_URL,
            decode_responses=True,
        )
