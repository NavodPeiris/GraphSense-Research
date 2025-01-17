from __future__ import annotations

from collections.abc import Iterable, Iterator
from dataclasses import dataclass


@dataclass
class Node:
    data: int
    next_node: Node | None = None


class LinkedList:

    def __init__(self) -> None:
        self.head: Node | None = None
        self.tail: Node | None = None  

    def __iter__(self) -> Iterator[int]:
        node = self.head
        while node:
            yield node.data
            node = node.next_node

    def __repr__(self) -> str:
        return " -> ".join([str(data) for data in self])

    def append(self, data: int) -> None:
        if self.tail:
            self.tail.next_node = self.tail = Node(data)
        else:
            self.head = self.tail = Node(data)

    def extend(self, items: Iterable[int]) -> None:
        for item in items:
            self.append(item)


def make_linked_list(elements_list: Iterable[int]) -> LinkedList:
    if not elements_list:
        raise Exception("The Elements List is empty")

    linked_list = LinkedList()
    linked_list.extend(elements_list)
    return linked_list


def in_reverse(linked_list: LinkedList) -> str:
    return " <- ".join(str(line) for line in reversed(tuple(linked_list)))


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    linked_list = make_linked_list((14, 52, 14, 12, 43))
    print(f"Linked List:  {linked_list}")
    print(f"Reverse List: {in_reverse(linked_list)}")
