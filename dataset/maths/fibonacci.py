
import functools
from collections.abc import Iterator
from math import sqrt
from time import time

import numpy as np
from numpy import ndarray


def time_func(func, *args, **kwargs):
    start = time()
    output = func(*args, **kwargs)
    end = time()
    if int(end - start) > 0:
        print(f"{func.__name__} runtime: {(end - start):0.4f} s")
    else:
        print(f"{func.__name__} runtime: {(end - start) * 1000:0.4f} ms")
    return output


def fib_iterative_yield(n: int) -> Iterator[int]:
    if n < 0:
        raise ValueError("n is negative")
    a, b = 0, 1
    yield a
    for _ in range(n):
        yield b
        a, b = b, a + b


def fib_iterative(n: int) -> list[int]:
    if n < 0:
        raise ValueError("n is negative")
    if n == 0:
        return [0]
    fib = [0, 1]
    for _ in range(n - 1):
        fib.append(fib[-1] + fib[-2])
    return fib


def fib_recursive(n: int) -> list[int]:

    def fib_recursive_term(i: int) -> int:
        if i < 0:
            raise ValueError("n is negative")
        if i < 2:
            return i
        return fib_recursive_term(i - 1) + fib_recursive_term(i - 2)

    if n < 0:
        raise ValueError("n is negative")
    return [fib_recursive_term(i) for i in range(n + 1)]


def fib_recursive_cached(n: int) -> list[int]:

    @functools.cache
    def fib_recursive_term(i: int) -> int:
        if i < 0:
            raise ValueError("n is negative")
        if i < 2:
            return i
        return fib_recursive_term(i - 1) + fib_recursive_term(i - 2)

    if n < 0:
        raise ValueError("n is negative")
    return [fib_recursive_term(i) for i in range(n + 1)]


def fib_memoization(n: int) -> list[int]:
    if n < 0:
        raise ValueError("n is negative")
    
    
    cache: dict[int, int] = {0: 0, 1: 1, 2: 1}  

    def rec_fn_memoized(num: int) -> int:
        if num in cache:
            return cache[num]

        value = rec_fn_memoized(num - 1) + rec_fn_memoized(num - 2)
        cache[num] = value
        return value

    return [rec_fn_memoized(i) for i in range(n + 1)]


def fib_binet(n: int) -> list[int]:
    if n < 0:
        raise ValueError("n is negative")
    if n >= 1475:
        raise ValueError("n is too large")
    sqrt_5 = sqrt(5)
    phi = (1 + sqrt_5) / 2
    return [round(phi**i / sqrt_5) for i in range(n + 1)]


def matrix_pow_np(m: ndarray, power: int) -> ndarray:
    result = np.array([[1, 0], [0, 1]], dtype=int)  
    base = m
    if power < 0:  
        raise ValueError("power is negative")
    while power:
        if power % 2 == 1:
            result = np.dot(result, base)
        base = np.dot(base, base)
        power //= 2
    return result


def fib_matrix_np(n: int) -> int:
    if n < 0:
        raise ValueError("n is negative")
    if n == 0:
        return 0

    m = np.array([[1, 1], [1, 0]], dtype=int)
    result = matrix_pow_np(m, n - 1)
    return int(result[0, 0])


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    
    num = 30
    time_func(fib_iterative_yield, num)  
    time_func(fib_iterative, num)  
    time_func(fib_binet, num)  
    time_func(fib_memoization, num)  
    time_func(fib_recursive_cached, num)  
    time_func(fib_recursive, num)  
    time_func(fib_matrix_np, num)
