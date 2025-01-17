
from collections.abc import Iterator
from dataclasses import dataclass


@dataclass
class Index2DArrayIterator:
    matrix: list[list[int]]

    def __iter__(self) -> Iterator[int]:
        
        for row in self.matrix:
            yield from row


def index_2d_array_in_1d(array: list[list[int]], index: int) -> int:
    
    rows = len(array)
    cols = len(array[0])

    if rows == 0 or cols == 0:
        raise ValueError("no items in array")

    if index < 0 or index >= rows * cols:
        raise ValueError("index out of range")

    return array[index // cols][index % cols]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
