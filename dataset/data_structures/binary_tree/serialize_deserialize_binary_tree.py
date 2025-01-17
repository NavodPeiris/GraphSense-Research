from __future__ import annotations

from collections.abc import Iterator
from dataclasses import dataclass


@dataclass
class TreeNode:
    
    value: int = 0
    left: TreeNode | None = None
    right: TreeNode | None = None

    def __post_init__(self):
        if not isinstance(self.value, int):
            raise TypeError("Value must be an integer.")

    def __iter__(self) -> Iterator[TreeNode]:
        
        yield self
        yield from self.left or ()
        yield from self.right or ()

    def __len__(self) -> int:
       
        return sum(1 for _ in self)

    def __repr__(self) -> str:
        
        return f"{self.value},{self.left!r},{self.right!r}".replace("None", "null")

    @classmethod
    def five_tree(cls) -> TreeNode:
        
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.right.left = TreeNode(4)
        root.right.right = TreeNode(5)
        return root


def deserialize(data: str) -> TreeNode | None:
    

    if not data:
        raise ValueError("Data cannot be empty.")

    
    nodes = data.split(",")

    def build_tree() -> TreeNode | None:
        
        value = nodes.pop(0)

        if value == "null":
            return None

        node = TreeNode(int(value))
        node.left = build_tree()  
        node.right = build_tree()  
        return node

    return build_tree()


if __name__ == "__main__":
    import doctest

    doctest.testmod()
