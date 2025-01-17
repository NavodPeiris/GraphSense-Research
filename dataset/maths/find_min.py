from __future__ import annotations


def find_min_iterative(nums: list[int | float]) -> int | float:
    if len(nums) == 0:
        raise ValueError("find_min_iterative() arg is an empty sequence")
    min_num = nums[0]
    for num in nums:
        min_num = min(min_num, num)
    return min_num



def find_min_recursive(nums: list[int | float], left: int, right: int) -> int | float:
    if len(nums) == 0:
        raise ValueError("find_min_recursive() arg is an empty sequence")
    if (
        left >= len(nums)
        or left < -len(nums)
        or right >= len(nums)
        or right < -len(nums)
    ):
        raise IndexError("list index out of range")
    if left == right:
        return nums[left]
    mid = (left + right) >> 1  
    left_min = find_min_recursive(nums, left, mid)  
    right_min = find_min_recursive(
        nums, mid + 1, right
    )  

    return left_min if left_min <= right_min else right_min


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
