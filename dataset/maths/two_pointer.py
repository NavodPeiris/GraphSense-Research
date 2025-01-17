
from __future__ import annotations


def two_pointer(nums: list[int], target: int) -> list[int]:
    i = 0
    j = len(nums) - 1

    while i < j:
        if nums[i] + nums[j] == target:
            return [i, j]
        elif nums[i] + nums[j] < target:
            i = i + 1
        else:
            j = j - 1

    return []


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(f"{two_pointer([2, 7, 11, 15], 9) = }")
