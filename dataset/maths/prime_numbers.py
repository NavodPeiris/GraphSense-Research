import math
from collections.abc import Generator


def slow_primes(max_n: int) -> Generator[int]:
    numbers: Generator = (i for i in range(1, (max_n + 1)))
    for i in (n for n in numbers if n > 1):
        for j in range(2, i):
            if (i % j) == 0:
                break
        else:
            yield i


def primes(max_n: int) -> Generator[int]:
    numbers: Generator = (i for i in range(1, (max_n + 1)))
    for i in (n for n in numbers if n > 1):
        
        bound = int(math.sqrt(i)) + 1
        for j in range(2, bound):
            if (i % j) == 0:
                break
        else:
            yield i


def fast_primes(max_n: int) -> Generator[int]:
    numbers: Generator = (i for i in range(1, (max_n + 1), 2))
    
    if max_n > 2:
        yield 2  
    for i in (n for n in numbers if n > 1):
        bound = int(math.sqrt(i)) + 1
        for j in range(3, bound, 2):
            
            if (i % j) == 0:
                break
        else:
            yield i


def benchmark():
    from timeit import timeit

    setup = "from __main__ import slow_primes, primes, fast_primes"
    print(timeit("slow_primes(1_000_000_000_000)", setup=setup, number=1_000_000))
    print(timeit("primes(1_000_000_000_000)", setup=setup, number=1_000_000))
    print(timeit("fast_primes(1_000_000_000_000)", setup=setup, number=1_000_000))


if __name__ == "__main__":
    number = int(input("Calculate primes up to:\n>> ").strip())
    for ret in primes(number):
        print(ret)
    benchmark()
