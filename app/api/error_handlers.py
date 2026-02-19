# app/api/error_handlers.py

from __future__ import annotations

import logging
from typing import Any, Dict

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.domain.errors import (
    DomainError,
    NotFoundError,
    ServiceError, 
    ValidationError
)
def _error_payload(
    code: str,
    message: str
) -> Dict[str, Any]:
    payload: Dict[str, Any] = {"code": code, "message": message}
    return payload


def _domain_to_http(exc: DomainError) -> tuple[int, Dict[str, Any]]:
    status_code = 400

    code = exc.code or "GEN_000"
    message = exc.message or str(exc) or "Unknown error"

    if isinstance(exc, NotFoundError):
        status_code = 404
    elif isinstance(exc, ValidationError):
        status_code = 409
    elif isinstance(exc, ServiceError):
        status_code = 500

    return status_code, _error_payload(code=code, message=message)


def register_exception_handlers(app: FastAPI) -> None:
    @app.exception_handler(DomainError)
    async def domain_error_handler(_: Request, exc: DomainError):
        status_code, payload = _domain_to_http(exc)
        return JSONResponse(status_code=status_code, content=payload)

    @app.exception_handler(Exception)
    async def unhandled_exception_handler(_: Request, exc: Exception):
        logging.error(f"Unhandled exception: {exc}", exc_info=True)
        payload = _error_payload(code="GEN_500", message="Internal server error")
        return JSONResponse(status_code=500, content=payload)
