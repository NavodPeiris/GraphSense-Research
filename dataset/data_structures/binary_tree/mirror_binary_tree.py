
from __future__ import annotations

from collections.abc import Iterator
from dataclasses import dataclass


@dataclass
class Node:
    
    value: int
    left: Node | None = None
    right: Node | None = None

    def __iter__(self) -> Iterator[int]:
        if self.left:
            yield from self.left
        yield self.value
        if self.right:
            yield from self.right

    def __len__(self) -> int:
        return sum(1 for _ in self)

    def mirror(self) -> Node:
       
        self.left, self.right = self.right, self.left
        if self.left:
            self.left.mirror()
        if self.right:
            self.right.mirror()
        return self


def make_tree_seven() -> Node:
    
    tree = Node(1)
    tree.left = Node(2)
    tree.right = Node(3)
    tree.left.left = Node(4)
    tree.left.right = Node(5)
    tree.right.left = Node(6)
    tree.right.right = Node(7)
    return tree


def make_tree_nine() -> Node:
   
    tree = Node(1)
    tree.left = Node(2)
    tree.right = Node(3)
    tree.left.left = Node(4)
    tree.left.right = Node(5)
    tree.right.right = Node(6)
    tree.left.left.left = Node(7)
    tree.left.left.right = Node(8)
    tree.left.right.right = Node(9)
    return tree


def main() -> None:
   
    trees = {"zero": Node(0), "seven": make_tree_seven(), "nine": make_tree_nine()}
    for name, tree in trees.items():
        print(f"      The {name} tree: {tuple(tree)}")
        
        print(f"Mirror of {name} tree: {tuple(tree.mirror())}")
        


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
