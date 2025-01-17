
from __future__ import annotations


def find_median(nums: list[int | float]) -> float:
    div, mod = divmod(len(nums), 2)
    if mod:
        return nums[div]
    return (nums[div] + nums[(div) - 1]) / 2


def interquartile_range(nums: list[int | float]) -> float:
    if not nums:
        raise ValueError("The list is empty. Provide a non-empty list.")
    nums.sort()
    length = len(nums)
    div, mod = divmod(length, 2)
    q1 = find_median(nums[:div])
    half_length = sum((div, mod))
    q3 = find_median(nums[half_length:length])
    return q3 - q1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
