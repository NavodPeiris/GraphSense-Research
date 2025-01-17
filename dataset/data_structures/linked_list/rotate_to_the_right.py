from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Node:
    data: int
    next_node: Node | None = None


def print_linked_list(head: Node | None) -> None:
    if head is None:
        return
    while head.next_node is not None:
        print(head.data, end="->")
        head = head.next_node
    print(head.data)


def insert_node(head: Node | None, data: int) -> Node:
    new_node = Node(data)
    
    if head is None:
        return new_node

    temp_node = head
    while temp_node.next_node:
        temp_node = temp_node.next_node

    temp_node.next_node = new_node
    return head


def rotate_to_the_right(head: Node, places: int) -> Node:
    
    if not head:
        raise ValueError("The linked list is empty.")

    if head.next_node is None:
        return head

    
    length = 1
    temp_node = head
    while temp_node.next_node is not None:
        length += 1
        temp_node = temp_node.next_node

    
    places %= length

    if places == 0:
        return head  

    
    new_head_index = length - places

    
    temp_node = head
    for _ in range(new_head_index - 1):
        assert temp_node.next_node
        temp_node = temp_node.next_node

    
    assert temp_node.next_node
    new_head = temp_node.next_node
    temp_node.next_node = None
    temp_node = new_head
    while temp_node.next_node:
        temp_node = temp_node.next_node
    temp_node.next_node = head

    assert new_head
    return new_head


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    head = insert_node(None, 5)
    head = insert_node(head, 1)
    head = insert_node(head, 2)
    head = insert_node(head, 4)
    head = insert_node(head, 3)

    print("Original list: ", end="")
    print_linked_list(head)

    places = 3
    new_head = rotate_to_the_right(head, places)

    print(f"After {places} iterations: ", end="")
    print_linked_list(new_head)
