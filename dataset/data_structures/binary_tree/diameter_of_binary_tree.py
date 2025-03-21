

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Node:
    data: int
    left: Node | None = None
    right: Node | None = None

    def depth(self) -> int:
        
        left_depth = self.left.depth() if self.left else 0
        right_depth = self.right.depth() if self.right else 0
        return max(left_depth, right_depth) + 1

    def diameter(self) -> int:
        
        left_depth = self.left.depth() if self.left else 0
        right_depth = self.right.depth() if self.right else 0
        return left_depth + right_depth + 1


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    
    print(f"{root.diameter() = }")  # 4
    print(f"{root.left.diameter() = }")  # 3
    print(f"{root.right.diameter() = }")  # 1
