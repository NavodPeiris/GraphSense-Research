
from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass
from typing import Any


class Deque:

    __slots__ = ("_back", "_front", "_len")

    @dataclass
    class _Node:

        val: Any = None
        next_node: Deque._Node | None = None
        prev_node: Deque._Node | None = None

    class _Iterator:

        __slots__ = ("_cur",)

        def __init__(self, cur: Deque._Node | None) -> None:
            self._cur = cur

        def __iter__(self) -> Deque._Iterator:
            return self

        def __next__(self) -> Any:
            if self._cur is None:
                
                raise StopIteration
            val = self._cur.val
            self._cur = self._cur.next_node

            return val

    def __init__(self, iterable: Iterable[Any] | None = None) -> None:
        self._front: Any = None
        self._back: Any = None
        self._len: int = 0

        if iterable is not None:
            
            for val in iterable:
                self.append(val)

    def append(self, val: Any) -> None:
        node = self._Node(val, None, None)
        if self.is_empty():
            
            self._front = self._back = node
            self._len = 1
        else:
            
            self._back.next_node = node
            node.prev_node = self._back
            self._back = node  

            self._len += 1

            
            assert not self.is_empty(), "Error on appending value."

    def appendleft(self, val: Any) -> None:
        node = self._Node(val, None, None)
        if self.is_empty():
            
            self._front = self._back = node
            self._len = 1
        else:
            
            node.next_node = self._front
            self._front.prev_node = node
            self._front = node  

            self._len += 1

            
            assert not self.is_empty(), "Error on appending value."

    def extend(self, iterable: Iterable[Any]) -> None:
        for val in iterable:
            self.append(val)

    def extendleft(self, iterable: Iterable[Any]) -> None:
        for val in iterable:
            self.appendleft(val)

    def pop(self) -> Any:
        
        assert not self.is_empty(), "Deque is empty."

        topop = self._back
        
        
        if self._front == self._back:
            self._front = None
            self._back = None
        else:
            self._back = self._back.prev_node  
            
            self._back.next_node = None

        self._len -= 1

        return topop.val

    def popleft(self) -> Any:
        
        assert not self.is_empty(), "Deque is empty."

        topop = self._front
        
        
        if self._front == self._back:
            self._front = None
            self._back = None
        else:
            self._front = self._front.next_node  
            self._front.prev_node = None

        self._len -= 1

        return topop.val

    def is_empty(self) -> bool:
        return self._front is None

    def __len__(self) -> int:
        return self._len

    def __eq__(self, other: object) -> bool:

        if not isinstance(other, Deque):
            return NotImplemented

        me = self._front
        oth = other._front

        
        if len(self) != len(other):
            return False

        while me is not None and oth is not None:
            
            if me.val != oth.val:
                return False
            me = me.next_node
            oth = oth.next_node

        return True

    def __iter__(self) -> Deque._Iterator:
        return Deque._Iterator(self._front)

    def __repr__(self) -> str:
        values_list = []
        aux = self._front
        while aux is not None:
            
            values_list.append(aux.val)
            aux = aux.next_node

        return f"[{', '.join(repr(val) for val in values_list)}]"


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    dq = Deque([3])
    dq.pop()
