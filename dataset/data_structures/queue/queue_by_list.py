
from collections.abc import Iterable
from typing import Generic, TypeVar

_T = TypeVar("_T")


class QueueByList(Generic[_T]):
    def __init__(self, iterable: Iterable[_T] | None = None) -> None:
        self.entries: list[_T] = list(iterable or [])

    def __len__(self) -> int:

        return len(self.entries)

    def __repr__(self) -> str:

        return f"Queue({tuple(self.entries)})"

    def put(self, item: _T) -> None:

        self.entries.append(item)

    def get(self) -> _T:

        if not self.entries:
            raise IndexError("Queue is empty")
        return self.entries.pop(0)

    def rotate(self, rotation: int) -> None:

        put = self.entries.append
        get = self.entries.pop

        for _ in range(rotation):
            put(get(0))

    def get_front(self) -> _T:

        return self.entries[0]


if __name__ == "__main__":
    from doctest import testmod

    testmod()
