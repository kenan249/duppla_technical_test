import asyncio

from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from app.infra.redis_client import RedisClient


class JobsWebSocketController:
    def __init__(self):
        self.redis_client = RedisClient()
        self.router = APIRouter(tags=["websocket"])
        
        self.router.add_api_websocket_route("/ws/jobs/{job_id}", self.job_updates)

    async def job_updates(self, websocket: WebSocket, job_id: str):
        await websocket.accept()
        
        pubsub = self.redis_client.get_redis_sync().pubsub()
        channel = f"job:{job_id}"
        pubsub.subscribe(channel)
        
        try:
            while True:
                message = pubsub.get_message(ignore_subscribe_messages=True, timeout=1.0)
                if message and message["type"] == "message":
                    data = message["data"]
                    if isinstance(data, bytes):
                        data = data.decode("utf-8")
                    await websocket.send_text(data)
                await asyncio.sleep(0.1)
        except WebSocketDisconnect:
            pass
        finally:
            pubsub.unsubscribe(channel)
            pubsub.close()


router = JobsWebSocketController().router