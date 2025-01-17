
from __future__ import annotations

from collections.abc import Iterator
from typing import Generic, TypeVar

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, data: T):
        self.data = data
        self.next: Node[T] | None = None

    def __str__(self) -> str:
        return f"{self.data}"


class LinkedStack(Generic[T]):

    def __init__(self) -> None:
        self.top: Node[T] | None = None

    def __iter__(self) -> Iterator[T]:
        node = self.top
        while node:
            yield node.data
            node = node.next

    def __str__(self) -> str:
        return "->".join([str(item) for item in self])

    def __len__(self) -> int:
        return len(tuple(iter(self)))

    def is_empty(self) -> bool:
        return self.top is None

    def push(self, item: T) -> None:
        node = Node(item)
        if not self.is_empty():
            node.next = self.top
        self.top = node

    def pop(self) -> T:
        if self.is_empty():
            raise IndexError("pop from empty stack")
        assert isinstance(self.top, Node)
        pop_node = self.top
        self.top = self.top.next
        return pop_node.data

    def peek(self) -> T:
        if self.is_empty():
            raise IndexError("peek from empty stack")

        assert self.top is not None
        return self.top.data

    def clear(self) -> None:
        self.top = None


if __name__ == "__main__":
    from doctest import testmod

    testmod()
