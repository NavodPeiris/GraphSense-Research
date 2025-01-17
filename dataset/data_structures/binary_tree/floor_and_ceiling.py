

from __future__ import annotations

from collections.abc import Iterator
from dataclasses import dataclass


@dataclass
class Node:
    key: int
    left: Node | None = None
    right: Node | None = None

    def __iter__(self) -> Iterator[int]:
        if self.left:
            yield from self.left
        yield self.key
        if self.right:
            yield from self.right

    def __len__(self) -> int:
        return sum(1 for _ in self)


def floor_ceiling(root: Node | None, key: int) -> tuple[int | None, int | None]:
    
    floor_val = None
    ceiling_val = None

    while root:
        if root.key == key:
            floor_val = root.key
            ceiling_val = root.key
            break

        if key < root.key:
            ceiling_val = root.key
            root = root.left
        else:
            floor_val = root.key
            root = root.right

    return floor_val, ceiling_val


if __name__ == "__main__":
    import doctest

    doctest.testmod()
