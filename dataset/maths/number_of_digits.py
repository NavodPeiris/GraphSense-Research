import math
from timeit import timeit


def num_digits(n: int) -> int:

    if not isinstance(n, int):
        raise TypeError("Input must be an integer")

    digits = 0
    n = abs(n)
    while True:
        n = n // 10
        digits += 1
        if n == 0:
            break
    return digits


def num_digits_fast(n: int) -> int:

    if not isinstance(n, int):
        raise TypeError("Input must be an integer")

    return 1 if n == 0 else math.floor(math.log(abs(n), 10) + 1)


def num_digits_faster(n: int) -> int:

    if not isinstance(n, int):
        raise TypeError("Input must be an integer")

    return len(str(abs(n)))


def benchmark() -> None:
    from collections.abc import Callable

    def benchmark_a_function(func: Callable, value: int) -> None:
        call = f"{func.__name__}({value})"
        timing = timeit(f"__main__.{call}", setup="import __main__")
        print(f"{call}: {func(value)} -- {timing} seconds")

    for value in (262144, 1125899906842624, 1267650600228229401496703205376):
        for func in (num_digits, num_digits_fast, num_digits_faster):
            benchmark_a_function(func, value)
        print()


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    benchmark()
