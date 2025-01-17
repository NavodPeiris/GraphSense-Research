def sum_of_digits(n: int) -> int:
    n = abs(n)
    res = 0
    while n > 0:
        res += n % 10
        n //= 10
    return res


def sum_of_digits_recursion(n: int) -> int:
    n = abs(n)
    return n if n < 10 else n % 10 + sum_of_digits(n // 10)


def sum_of_digits_compact(n: int) -> int:
    return sum(int(c) for c in str(abs(n)))


def benchmark() -> None:
    from collections.abc import Callable
    from timeit import timeit

    def benchmark_a_function(func: Callable, value: int) -> None:
        call = f"{func.__name__}({value})"
        timing = timeit(f"__main__.{call}", setup="import __main__")
        print(f"{call:56} = {func(value)} -- {timing:.4f} seconds")

    for value in (262144, 1125899906842624, 1267650600228229401496703205376):
        for func in (sum_of_digits, sum_of_digits_recursion, sum_of_digits_compact):
            benchmark_a_function(func, value)
        print()


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    benchmark()
