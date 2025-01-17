
from __future__ import annotations


def max_sum_in_array(array: list[int], k: int) -> int:
    if len(array) < k or k < 0:
        raise ValueError("Invalid Input")
    max_sum = current_sum = sum(array[:k])
    for i in range(len(array) - k):
        current_sum = current_sum - array[i] + array[i + k]
        max_sum = max(max_sum, current_sum)
    return max_sum


if __name__ == "__main__":
    from doctest import testmod
    from random import randint

    testmod()
    array = [randint(-1000, 1000) for i in range(100)]
    k = randint(0, 110)
    print(
        f"The maximum sum of {k} consecutive elements is {max_sum_in_array(array, k)}"
    )
