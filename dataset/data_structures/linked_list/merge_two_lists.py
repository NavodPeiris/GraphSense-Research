
from __future__ import annotations

from collections.abc import Iterable, Iterator
from dataclasses import dataclass

test_data_odd = (3, 9, -11, 0, 7, 5, 1, -1)
test_data_even = (4, 6, 2, 0, 8, 10, 3, -2)


@dataclass
class Node:
    data: int
    next_node: Node | None


class SortedLinkedList:
    def __init__(self, ints: Iterable[int]) -> None:
        self.head: Node | None = None
        for i in sorted(ints, reverse=True):
            self.head = Node(i, self.head)

    def __iter__(self) -> Iterator[int]:
        node = self.head
        while node:
            yield node.data
            node = node.next_node

    def __len__(self) -> int:
        return sum(1 for _ in self)

    def __str__(self) -> str:
        return " -> ".join([str(node) for node in self])


def merge_lists(
    sll_one: SortedLinkedList, sll_two: SortedLinkedList
) -> SortedLinkedList:
    return SortedLinkedList(list(sll_one) + list(sll_two))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    SSL = SortedLinkedList
    print(merge_lists(SSL(test_data_odd), SSL(test_data_even)))
