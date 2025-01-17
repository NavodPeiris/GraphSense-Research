

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Node:
    

    data: int
    left: Node | None = None
    right: Node | None = None


def make_symmetric_tree() -> Node:
   
    root = Node(1)
    root.left = Node(2)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(4)
    root.right.right = Node(3)
    return root


def make_asymmetric_tree() -> Node:
    
    root = Node(1)
    root.left = Node(2)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(3)
    root.right.right = Node(4)
    return root


def is_symmetric_tree(tree: Node) -> bool:

    if tree:
        return is_mirror(tree.left, tree.right)
    return True  


def is_mirror(left: Node | None, right: Node | None) -> bool:
    
    if left is None and right is None:
        
        return True
    if left is None or right is None:
        
        return False
    if left.data == right.data:
       
        return is_mirror(left.left, right.right) and is_mirror(left.right, right.left)
    return False


if __name__ == "__main__":
    from doctest import testmod

    testmod()
