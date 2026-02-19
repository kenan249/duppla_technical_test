from fastapi import FastAPI
from app.api.error_handlers import register_exception_handlers
from app.api.routers import documents, jobs, batch
from app.api.ws import jobs_ws


app = FastAPI(
    title="Document Management API",
    version="1.0.0",
)
register_exception_handlers(app)
app.include_router(documents.router)
app.include_router(jobs.router)
app.include_router(batch.router)
app.include_router(jobs_ws.router)
