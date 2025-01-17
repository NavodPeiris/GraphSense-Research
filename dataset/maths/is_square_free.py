
from __future__ import annotations


def is_square_free(factors: list[int]) -> bool:
    return len(set(factors)) == len(factors)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
