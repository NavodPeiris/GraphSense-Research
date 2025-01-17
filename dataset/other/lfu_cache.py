from __future__ import annotations

from collections.abc import Callable
from typing import Generic, TypeVar

T = TypeVar("T")
U = TypeVar("U")


class DoubleLinkedListNode(Generic[T, U]):

    def __init__(self, key: T | None, val: U | None):
        self.key = key
        self.val = val
        self.freq: int = 0
        self.next: DoubleLinkedListNode[T, U] | None = None
        self.prev: DoubleLinkedListNode[T, U] | None = None

    def __repr__(self) -> str:
        return (
            f"Node: key: {self.key}, val: {self.val}, freq: {self.freq}, "
            f"has next: {self.next is not None}, has prev: {self.prev is not None}"
        )


class DoubleLinkedList(Generic[T, U]):

    def __init__(self) -> None:
        self.head: DoubleLinkedListNode[T, U] = DoubleLinkedListNode(None, None)
        self.rear: DoubleLinkedListNode[T, U] = DoubleLinkedListNode(None, None)
        self.head.next, self.rear.prev = self.rear, self.head

    def __repr__(self) -> str:
        rep = ["DoubleLinkedList"]
        node = self.head
        while node.next is not None:
            rep.append(str(node))
            node = node.next
        rep.append(str(self.rear))
        return ",\n    ".join(rep)

    def add(self, node: DoubleLinkedListNode[T, U]) -> None:

        previous = self.rear.prev

        
        assert previous is not None

        previous.next = node
        node.prev = previous
        self.rear.prev = node
        node.next = self.rear
        node.freq += 1
        self._position_node(node)

    def _position_node(self, node: DoubleLinkedListNode[T, U]) -> None:

        while node.prev is not None and node.prev.freq > node.freq:
            
            previous_node = node.prev

            node.prev = previous_node.prev
            previous_node.next = node.prev
            node.next = previous_node
            previous_node.prev = node

    def remove(
        self, node: DoubleLinkedListNode[T, U]
    ) -> DoubleLinkedListNode[T, U] | None:

        if node.prev is None or node.next is None:
            return None

        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = None
        node.next = None
        return node


class LFUCache(Generic[T, U]):

    
    decorator_function_to_instance_map: dict[Callable[[T], U], LFUCache[T, U]] = {}

    def __init__(self, capacity: int):
        self.list: DoubleLinkedList[T, U] = DoubleLinkedList()
        self.capacity = capacity
        self.num_keys = 0
        self.hits = 0
        self.miss = 0
        self.cache: dict[T, DoubleLinkedListNode[T, U]] = {}

    def __repr__(self) -> str:

        return (
            f"CacheInfo(hits={self.hits}, misses={self.miss}, "
            f"capacity={self.capacity}, current_size={self.num_keys})"
        )

    def __contains__(self, key: T) -> bool:

        return key in self.cache

    def get(self, key: T) -> U | None:

        if key in self.cache:
            self.hits += 1
            value_node: DoubleLinkedListNode[T, U] = self.cache[key]
            node = self.list.remove(self.cache[key])
            assert node == value_node

            
            assert node is not None
            self.list.add(node)
            return node.val
        self.miss += 1
        return None

    def put(self, key: T, value: U) -> None:

        if key not in self.cache:
            if self.num_keys >= self.capacity:
                
                first_node = self.list.head.next

                
                
                assert first_node is not None
                assert first_node.key is not None
                assert self.list.remove(first_node) is not None
                

                del self.cache[first_node.key]
                self.num_keys -= 1
            self.cache[key] = DoubleLinkedListNode(key, value)
            self.list.add(self.cache[key])
            self.num_keys += 1

        else:
            node = self.list.remove(self.cache[key])
            assert node is not None  
            node.val = value
            self.list.add(node)

    @classmethod
    def decorator(
        cls: type[LFUCache[T, U]], size: int = 128
    ) -> Callable[[Callable[[T], U]], Callable[..., U]]:

        def cache_decorator_inner(func: Callable[[T], U]) -> Callable[..., U]:
            def cache_decorator_wrapper(*args: T) -> U:
                if func not in cls.decorator_function_to_instance_map:
                    cls.decorator_function_to_instance_map[func] = LFUCache(size)

                result = cls.decorator_function_to_instance_map[func].get(args[0])
                if result is None:
                    result = func(*args)
                    cls.decorator_function_to_instance_map[func].put(args[0], result)
                return result

            def cache_info() -> LFUCache[T, U]:
                return cls.decorator_function_to_instance_map[func]

            setattr(cache_decorator_wrapper, "cache_info", cache_info)  

            return cache_decorator_wrapper

        return cache_decorator_inner


if __name__ == "__main__":
    import doctest

    doctest.testmod()
