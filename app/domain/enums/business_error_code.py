from enum import Enum
from typing import Tuple

class BusinessErrorCode(Enum):
    DOC_001 = ("DOC_001", "Document not found")
    DOC_002 = ("DOC_002", "Invalid document status transition")
    DOC_003 = ("DOC_003", "Invalid document payload")
    DOC_004 = ("DOC_004", "Document status invalid for operation")

    JOB_001 = ("JOB_001", "Job not found")
    JOB_002 = ("JOB_002", "Invalid job state")
    JOB_003 = ("JOB_003", "Batch processing failed")
    JOB_004 = ("JOB_004", "Invalid progress out of range [0, total]")

    AUTH_001 = ("AUTH_001", "Unauthorized")
    RATE_001 = ("RATE_001", "Rate limit exceeded")

    @property
    def code(self) -> str:
        return self.value[0]

    @property
    def message(self) -> str:
        return self.value[1]

    def as_dict(self) -> dict:
        return {"code": self.code, "message": self.message}

    @staticmethod
    def from_tuple(item: Tuple[str, str]) -> "BusinessErrorCode":
        return BusinessErrorCode(item)