

from functools import lru_cache


@lru_cache
def factorial(num: int) -> int:
    if num < 0:
        raise ValueError("Number should not be negative.")

    return 1 if num in (0, 1) else num * factorial(num - 1)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
