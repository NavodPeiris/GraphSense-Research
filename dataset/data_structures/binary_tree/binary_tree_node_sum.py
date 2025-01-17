

from __future__ import annotations

from collections.abc import Iterator


class Node:
    

    def __init__(self, value: int) -> None:
        self.value = value
        self.left: Node | None = None
        self.right: Node | None = None


class BinaryTreeNodeSum:
    

    def __init__(self, tree: Node) -> None:
        self.tree = tree

    def depth_first_search(self, node: Node | None) -> int:
        if node is None:
            return 0
        return node.value + (
            self.depth_first_search(node.left) + self.depth_first_search(node.right)
        )

    def __iter__(self) -> Iterator[int]:
        yield self.depth_first_search(self.tree)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
