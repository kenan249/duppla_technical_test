
import logging
import os
import dotenv

from rq import Worker, Queue

from app.infra.redis_client import RedisClient
from app.infra.settings import DOCUMENT_BATCH_QUEUE_NAME

logger = logging.getLogger(__name__)

def run() -> None:
    dotenv.load_dotenv()
    redis_conn =RedisClient().get_redis_rq_sync()
    logger.info(f"Starting RQ worker. Listening to queue: {DOCUMENT_BATCH_QUEUE_NAME}")
    
    q = Queue(DOCUMENT_BATCH_QUEUE_NAME, connection=redis_conn)
    worker = Worker([q], connection=redis_conn)
    worker.work(with_scheduler=False)

if __name__ == "__main__":
    logging.basicConfig(level=os.getenv("LOG_LEVEL", "INFO"))
    run()
