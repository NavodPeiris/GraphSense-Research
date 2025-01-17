
from collections.abc import Sequence


def max_subarray_sum(
    arr: Sequence[float], allow_empty_subarrays: bool = False
) -> float:
    if not arr:
        return 0

    max_sum = 0 if allow_empty_subarrays else float("-inf")
    curr_sum = 0.0
    for num in arr:
        curr_sum = max(0 if allow_empty_subarrays else num, curr_sum + num)
        max_sum = max(max_sum, curr_sum)

    return max_sum


if __name__ == "__main__":
    from doctest import testmod

    testmod()

    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(f"{max_subarray_sum(nums) = }")
