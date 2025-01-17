

class Node:
    def __init__(self, data: int, previous=None, next_node=None):
        self.data = data
        self.previous = previous
        self.next = next_node

    def __str__(self) -> str:
        return f"{self.data}"

    def get_data(self) -> int:
        return self.data

    def get_next(self):
        return self.next

    def get_previous(self):
        return self.previous


class LinkedListIterator:
    def __init__(self, head):
        self.current = head

    def __iter__(self):
        return self

    def __next__(self):
        if not self.current:
            raise StopIteration
        else:
            value = self.current.get_data()
            self.current = self.current.get_next()
            return value


class LinkedList:
    def __init__(self):
        self.head = None  
        self.tail = None  

    def __str__(self):
        current = self.head
        nodes = []
        while current is not None:
            nodes.append(current.get_data())
            current = current.get_next()
        return " ".join(str(node) for node in nodes)

    def __contains__(self, value: int):
        current = self.head
        while current:
            if current.get_data() == value:
                return True
            current = current.get_next()
        return False

    def __iter__(self):
        return LinkedListIterator(self.head)

    def get_head_data(self):
        if self.head:
            return self.head.get_data()
        return None

    def get_tail_data(self):
        if self.tail:
            return self.tail.get_data()
        return None

    def set_head(self, node: Node) -> None:
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.insert_before_node(self.head, node)

    def set_tail(self, node: Node) -> None:
        if self.head is None:
            self.set_head(node)
        else:
            self.insert_after_node(self.tail, node)

    def insert(self, value: int) -> None:
        node = Node(value)
        if self.head is None:
            self.set_head(node)
        else:
            self.set_tail(node)

    def insert_before_node(self, node: Node, node_to_insert: Node) -> None:
        node_to_insert.next = node
        node_to_insert.previous = node.previous

        if node.get_previous() is None:
            self.head = node_to_insert
        else:
            node.previous.next = node_to_insert

        node.previous = node_to_insert

    def insert_after_node(self, node: Node, node_to_insert: Node) -> None:
        node_to_insert.previous = node
        node_to_insert.next = node.next

        if node.get_next() is None:
            self.tail = node_to_insert
        else:
            node.next.previous = node_to_insert

        node.next = node_to_insert

    def insert_at_position(self, position: int, value: int) -> None:
        current_position = 1
        new_node = Node(value)
        node = self.head
        while node:
            if current_position == position:
                self.insert_before_node(node, new_node)
                return
            current_position += 1
            node = node.next
        self.insert_after_node(self.tail, new_node)

    def get_node(self, item: int) -> Node:
        node = self.head
        while node:
            if node.get_data() == item:
                return node
            node = node.get_next()
        raise Exception("Node not found")

    def delete_value(self, value):
        if (node := self.get_node(value)) is not None:
            if node == self.head:
                self.head = self.head.get_next()

            if node == self.tail:
                self.tail = self.tail.get_previous()

            self.remove_node_pointers(node)

    @staticmethod
    def remove_node_pointers(node: Node) -> None:
        if node.get_next():
            node.next.previous = node.previous

        if node.get_previous():
            node.previous.next = node.next

        node.next = None
        node.previous = None

    def is_empty(self):
        return self.head is None


def create_linked_list() -> None:
    pass

if __name__ == "__main__":
    import doctest

    doctest.testmod()
