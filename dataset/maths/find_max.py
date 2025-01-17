from __future__ import annotations


def find_max_iterative(nums: list[int | float]) -> int | float:
    if len(nums) == 0:
        raise ValueError("find_max_iterative() arg is an empty sequence")
    max_num = nums[0]
    for x in nums:
        if x > max_num:  
            max_num = x
    return max_num



def find_max_recursive(nums: list[int | float], left: int, right: int) -> int | float:
    if len(nums) == 0:
        raise ValueError("find_max_recursive() arg is an empty sequence")
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
    left_max = find_max_recursive(nums, left, mid)  
    right_max = find_max_recursive(
        nums, mid + 1, right
    )  

    return left_max if left_max >= right_max else right_max


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
