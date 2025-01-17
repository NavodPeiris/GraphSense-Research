

class BinaryTreeNode:
   

    def __init__(self, data: int) -> None:
        self.data = data
        self.left_child: BinaryTreeNode | None = None
        self.right_child: BinaryTreeNode | None = None


def insert(node: BinaryTreeNode | None, new_value: int) -> BinaryTreeNode | None:
    
    if node is None:
        node = BinaryTreeNode(new_value)
        return node

    
    if new_value < node.data:
        node.left_child = insert(node.left_child, new_value)
    else:
        
        node.right_child = insert(node.right_child, new_value)
    return node


def inorder(node: None | BinaryTreeNode) -> list[int]:  
    
    if node:
        inorder_array = inorder(node.left_child)
        inorder_array = [*inorder_array, node.data]
        inorder_array = inorder_array + inorder(node.right_child)
    else:
        inorder_array = []
    return inorder_array


def make_tree() -> BinaryTreeNode | None:
    root = insert(None, 15)
    insert(root, 10)
    insert(root, 25)
    insert(root, 6)
    insert(root, 14)
    insert(root, 20)
    insert(root, 60)
    return root


def main() -> None:
    
    root = make_tree()
    print("Printing values of binary search tree in Inorder Traversal.")
    inorder(root)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
