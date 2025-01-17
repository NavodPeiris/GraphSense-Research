


from __future__ import annotations

from typing import Generic, TypeVar

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, data: T):
        self.data = data  
        self.next: Node[T] | None = None  
        self.prev: Node[T] | None = None  


class Stack(Generic[T]):

    def __init__(self) -> None:
        self.head: Node[T] | None = None

    def push(self, data: T) -> None:
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            new_node.prev = None
            self.head = new_node

    def pop(self) -> T | None:
        if self.head is None:
            return None
        else:
            assert self.head is not None
            temp = self.head.data
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
            return temp

    def top(self) -> T | None:
        return self.head.data if self.head is not None else None

    def __len__(self) -> int:
        temp = self.head
        count = 0
        while temp is not None:
            count += 1
            temp = temp.next
        return count

    def is_empty(self) -> bool:
        return self.head is None

    def print_stack(self) -> None:
        print("stack elements are:")
        temp = self.head
        while temp is not None:
            print(temp.data, end="->")
            temp = temp.next



if __name__ == "__main__":
    
    stack: Stack[int] = Stack()

    
    print("Stack operations using Doubly LinkedList")
    stack.push(4)

    
    stack.push(5)

    
    stack.push(6)

    
    stack.push(7)

    
    stack.print_stack()

    
    print("\nTop element is ", stack.top())

    
    print("Size of the stack is ", len(stack))

    
    stack.pop()

    
    stack.pop()

    
    stack.print_stack()

    
    print("\nstack is empty:", stack.is_empty())
