from dataclasses import dataclass
from typing import Generic, TypeVar, List

T = TypeVar("T")


@dataclass
class Page(Generic[T]):

    items: List[T]
    total: int
    page: int
    page_size: int

    @classmethod
    def from_list(cls, items: List[T], page: int = 1, page_size: int = 10) -> "Page[T]":
        total = len(items)
        start = (page - 1) * page_size
        end = start + page_size
        return cls(
            items=items[start:end],
            total=total,
            page=page,
            page_size=page_size,
        )

    @property
    def total_pages(self) -> int:
        if self.page_size <= 0:
            return 0
        return (self.total + self.page_size - 1) // self.page_size

    @property
    def has_next(self) -> bool:
        return self.page < self.total_pages

    @property
    def has_previous(self) -> bool:
        return self.page > 1
