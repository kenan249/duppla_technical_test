from dataclasses import dataclass
from typing import List


@dataclass
class BatchResult:
    total: int
    updated: int
    failed: int
    errors: List[dict]
