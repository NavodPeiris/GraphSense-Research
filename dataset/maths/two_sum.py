
from __future__ import annotations


def two_sum(nums: list[int], target: int) -> list[int]:
    chk_map: dict[int, int] = {}
    for index, val in enumerate(nums):
        compl = target - val
        if compl in chk_map:
            return [chk_map[compl], index]
        chk_map[val] = index
    return []


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(f"{two_sum([2, 7, 11, 15], 9) = }")
