
from __future__ import annotations

from itertools import combinations


def combination_lists(n: int, k: int) -> list[list[int]]:
    
    return [list(x) for x in combinations(range(1, n + 1), k)]


def generate_all_combinations(n: int, k: int) -> list[list[int]]:
    
    if k < 0:
        raise ValueError("k must not be negative")
    if n < 0:
        raise ValueError("n must not be negative")

    result: list[list[int]] = []
    create_all_state(1, n, k, [], result)
    return result


def create_all_state(
    increment: int,
    total_number: int,
    level: int,
    current_list: list[int],
    total_list: list[list[int]],
) -> None:
    
    if level == 0:
        total_list.append(current_list[:])
        return

    for i in range(increment, total_number - level + 2):
        current_list.append(i)
        create_all_state(i + 1, total_number, level - 1, current_list, total_list)
        current_list.pop()


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    print(generate_all_combinations(n=4, k=2))
    tests = ((n, k) for n in range(1, 5) for k in range(1, 5))
    for n, k in tests:
        print(n, k, generate_all_combinations(n, k) == combination_lists(n, k))

    print("Benchmark:")
    from timeit import timeit

    for func in ("combination_lists", "generate_all_combinations"):
        print(f"{func:>25}(): {timeit(f'{func}(n=4, k = 2)', globals=globals())}")
