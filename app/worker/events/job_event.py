from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class JobEvent:
    status: str
    processed: int
    total: int
    target_status: str
    current_document_id: Optional[str] = None
    result: Optional[str] = None
    reason: Optional[str] = None
    succeeded: Optional[int] = None
    failed: Optional[int] = None
    error: Optional[str] = None
    message: Optional[str] = None

    def to_dict(self) -> dict:
        payload = {
            "status": self.status,
            "processed": self.processed,
            "total": self.total,
            "target_status": self.target_status,
        }
        for k in (
            "current_document_id",
            "result",
            "reason",
            "succeeded",
            "failed",
            "error",
            "message",
        ):
            v = getattr(self, k)
            if v is not None:
                payload[k] = v
        return payload
