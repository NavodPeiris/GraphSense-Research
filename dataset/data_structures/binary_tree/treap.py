from __future__ import annotations

from random import random


class Node:
    

    def __init__(self, value: int | None = None):
        self.value = value
        self.prior = random()
        self.left: Node | None = None
        self.right: Node | None = None

    def __repr__(self) -> str:
        from pprint import pformat

        if self.left is None and self.right is None:
            return f"'{self.value}: {self.prior:.5}'"
        else:
            return pformat(
                {f"{self.value}: {self.prior:.5}": (self.left, self.right)}, indent=1
            )

    def __str__(self) -> str:
        value = str(self.value) + " "
        left = str(self.left or "")
        right = str(self.right or "")
        return value + left + right


def split(root: Node | None, value: int) -> tuple[Node | None, Node | None]:
    
    if root is None or root.value is None:  
        return None, None
    elif value < root.value:
        
        left, root.left = split(root.left, value)
        return left, root
    else:
        
        root.right, right = split(root.right, value)
        return root, right


def merge(left: Node | None, right: Node | None) -> Node | None:
    
    if (not left) or (not right):  
        return left or right
    elif left.prior < right.prior:
        
        left.right = merge(left.right, right)
        return left
    else:
        
        right.left = merge(left, right.left)
        return right


def insert(root: Node | None, value: int) -> Node | None:
    
    node = Node(value)
    left, right = split(root, value)
    return merge(merge(left, node), right)


def erase(root: Node | None, value: int) -> Node | None:
    
    left, right = split(root, value - 1)
    _, right = split(right, value)
    return merge(left, right)


def inorder(root: Node | None) -> None:
   
    if not root: 
        return
    else:
        inorder(root.left)
        print(root.value, end=",")
        inorder(root.right)


def interact_treap(root: Node | None, args: str) -> Node | None:
    
    for arg in args.split():
        if arg[0] == "+":
            root = insert(root, int(arg[1:]))

        elif arg[0] == "-":
            root = erase(root, int(arg[1:]))

        else:
            print("Unknown command")

    return root


def main() -> None:
    
    root = None
    print(
        "enter numbers to create a tree, + value to add value into treap, "
        "- value to erase all nodes with value. 'q' to quit. "
    )

    args = input()
    while args != "q":
        root = interact_treap(root, args)
        print(root)
        args = input()

    print("good by!")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
