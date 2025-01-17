
from __future__ import annotations

from itertools import permutations
from random import randint
from timeit import repeat


def make_dataset() -> tuple[list[int], int]:
    arr = [randint(-1000, 1000) for i in range(10)]
    r = randint(-5000, 5000)
    return (arr, r)


dataset = make_dataset()


def triplet_sum1(arr: list[int], target: int) -> tuple[int, ...]:
    for triplet in permutations(arr, 3):
        if sum(triplet) == target:
            return tuple(sorted(triplet))
    return (0, 0, 0)


def triplet_sum2(arr: list[int], target: int) -> tuple[int, int, int]:
    arr.sort()
    n = len(arr)
    for i in range(n - 1):
        left, right = i + 1, n - 1
        while left < right:
            if arr[i] + arr[left] + arr[right] == target:
                return (arr[i], arr[left], arr[right])
            elif arr[i] + arr[left] + arr[right] < target:
                left += 1
            elif arr[i] + arr[left] + arr[right] > target:
                right -= 1
    return (0, 0, 0)


def solution_times() -> tuple[float, float]:
    setup_code = """
from __main__ import dataset, triplet_sum1, triplet_sum2
    test_code2 = """
triplet_sum2(*dataset)
