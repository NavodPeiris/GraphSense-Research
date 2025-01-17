from __future__ import annotations

from typing import Generic, TypeVar

T = TypeVar("T")


class StackOverflowError(BaseException):
    pass


class StackUnderflowError(BaseException):
    pass


class Stack(Generic[T]):

    def __init__(self, limit: int = 10):
        self.stack: list[T] = []
        self.limit = limit

    def __bool__(self) -> bool:
        return bool(self.stack)

    def __str__(self) -> str:
        return str(self.stack)

    def push(self, data: T) -> None:
        if len(self.stack) >= self.limit:
            raise StackOverflowError
        self.stack.append(data)

    def pop(self) -> T:
        if not self.stack:
            raise StackUnderflowError
        return self.stack.pop()

    def peek(self) -> T:
        if not self.stack:
            raise StackUnderflowError
        return self.stack[-1]

    def is_empty(self) -> bool:
        return not bool(self.stack)

    def is_full(self) -> bool:
        return self.size() == self.limit

    def size(self) -> int:
        return len(self.stack)

    def __contains__(self, item: T) -> bool:
        return item in self.stack


def test_stack() -> None:
    stack: Stack[int] = Stack(10)
    assert bool(stack) is False
    assert stack.is_empty() is True
    assert stack.is_full() is False
    assert str(stack) == "[]"

    try:
        _ = stack.pop()
        raise AssertionError  
    except StackUnderflowError:
        assert True  

    try:
        _ = stack.peek()
        raise AssertionError  
    except StackUnderflowError:
        assert True  

    for i in range(10):
        assert stack.size() == i
        stack.push(i)

    assert bool(stack)
    assert not stack.is_empty()
    assert stack.is_full()
    assert str(stack) == str(list(range(10)))
    assert stack.pop() == 9
    assert stack.peek() == 8

    stack.push(100)
    assert str(stack) == str([0, 1, 2, 3, 4, 5, 6, 7, 8, 100])

    try:
        stack.push(200)
        raise AssertionError  
    except StackOverflowError:
        assert True  

    assert not stack.is_empty()
    assert stack.size() == 10

    assert 5 in stack
    assert 55 not in stack


if __name__ == "__main__":
    test_stack()

    import doctest

    doctest.testmod()
