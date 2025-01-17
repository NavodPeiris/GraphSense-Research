
from __future__ import annotations


class TreeNode:
    

    def __init__(self, data: int) -> None:
        self.data = data
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None


def build_tree() -> TreeNode:
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(6)
    return root


def flatten(root: TreeNode | None) -> None:
    
    if not root:
        return

    
    flatten(root.left)

    
    right_subtree = root.right

    
    root.right = root.left
    root.left = None

    
    current = root
    while current.right:
        current = current.right

    
    current.right = right_subtree

    
    flatten(right_subtree)


def display_linked_list(root: TreeNode | None) -> None:
    
    current = root
    while current:
        if current.right is None:
            print(current.data, end="")
            break
        print(current.data, end=" ")
        current = current.right


if __name__ == "__main__":
    print("Flattened Linked List:")
    root = build_tree()
    flatten(root)
    display_linked_list(root)
