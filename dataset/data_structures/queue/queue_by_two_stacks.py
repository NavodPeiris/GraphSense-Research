
from collections.abc import Iterable
from typing import Generic, TypeVar

_T = TypeVar("_T")


class QueueByTwoStacks(Generic[_T]):
    def __init__(self, iterable: Iterable[_T] | None = None) -> None:
        self._stack1: list[_T] = list(iterable or [])
        self._stack2: list[_T] = []

    def __len__(self) -> int:

        return len(self._stack1) + len(self._stack2)

    def __repr__(self) -> str:
        return f"Queue({tuple(self._stack2[::-1] + self._stack1)})"

    def put(self, item: _T) -> None:

        self._stack1.append(item)

    def get(self) -> _T:

        
        stack1_pop = self._stack1.pop
        stack2_append = self._stack2.append

        if not self._stack2:
            while self._stack1:
                stack2_append(stack1_pop())

        if not self._stack2:
            raise IndexError("Queue is empty")
        return self._stack2.pop()


if __name__ == "__main__":
    from doctest import testmod

    testmod()
