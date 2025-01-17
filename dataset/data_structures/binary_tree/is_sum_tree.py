

from __future__ import annotations

from collections.abc import Iterator
from dataclasses import dataclass


@dataclass
class Node:
    data: int
    left: Node | None = None
    right: Node | None = None

    def __iter__(self) -> Iterator[int]:

        if self.left:
            yield from self.left
        yield self.data
        if self.right:
            yield from self.right

    def __len__(self) -> int:
        
        return sum(1 for _ in self)

    @property
    def is_sum_node(self) -> bool:
        
        if not self.left and not self.right:
            return True 
        left_sum = sum(self.left) if self.left else 0
        right_sum = sum(self.right) if self.right else 0
        return all(
            (
                self.data == left_sum + right_sum,
                self.left.is_sum_node if self.left else True,
                self.right.is_sum_node if self.right else True,
            )
        )


@dataclass
class BinaryTree:
    root: Node

    def __iter__(self) -> Iterator[int]:
        
        return iter(self.root)

    def __len__(self) -> int:
        
        return len(self.root)

    def __str__(self) -> str:
        
        return str(list(self))

    @property
    def is_sum_tree(self) -> bool:
       
        return self.root.is_sum_node

    @classmethod
    def build_a_tree(cls) -> BinaryTree:
        
        tree = BinaryTree(Node(11))
        root = tree.root
        root.left = Node(2)
        root.right = Node(29)
        root.left.left = Node(1)
        root.left.right = Node(7)
        root.right.left = Node(15)
        root.right.right = Node(40)
        root.right.right.left = Node(35)
        return tree

    @classmethod
    def build_a_sum_tree(cls) -> BinaryTree:
        
        tree = BinaryTree(Node(26))
        root = tree.root
        root.left = Node(10)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(6)
        root.right.right = Node(3)
        return tree


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    tree = BinaryTree.build_a_tree()
    print(f"{tree} has {len(tree)} nodes and {tree.is_sum_tree = }.")
    tree = BinaryTree.build_a_sum_tree()
    print(f"{tree} has {len(tree)} nodes and {tree.is_sum_tree = }.")
