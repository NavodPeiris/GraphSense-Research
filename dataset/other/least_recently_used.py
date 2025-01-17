from __future__ import annotations

import sys
from collections import deque
from typing import Generic, TypeVar

T = TypeVar("T")


class LRUCache(Generic[T]):

    dq_store: deque[T]  
    key_reference: set[T]  
    _MAX_CAPACITY: int = 10  

    def __init__(self, n: int) -> None:
        self.dq_store = deque()
        self.key_reference = set()
        if not n:
            LRUCache._MAX_CAPACITY = sys.maxsize
        elif n < 0:
            raise ValueError("n should be an integer greater than 0.")
        else:
            LRUCache._MAX_CAPACITY = n

    def refer(self, x: T) -> None:
        if x not in self.key_reference:
            if len(self.dq_store) == LRUCache._MAX_CAPACITY:
                last_element = self.dq_store.pop()
                self.key_reference.remove(last_element)
        else:
            self.dq_store.remove(x)

        self.dq_store.appendleft(x)
        self.key_reference.add(x)

    def display(self) -> None:
        for k in self.dq_store:
            print(k)

    def __repr__(self) -> str:
        return f"LRUCache({self._MAX_CAPACITY}) => {list(self.dq_store)}"


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    lru_cache: LRUCache[str | int] = LRUCache(4)
    lru_cache.refer("A")
    lru_cache.refer(2)
    lru_cache.refer(3)
    lru_cache.refer("A")
    lru_cache.refer(4)
    lru_cache.refer(5)
    lru_cache.display()

    print(lru_cache)
    assert str(lru_cache) == "LRUCache(4) => [5, 4, 'A', 3]"
