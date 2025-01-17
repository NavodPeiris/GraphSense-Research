from __future__ import annotations


def mean(nums: list) -> float:
    if not nums:
        raise ValueError("List is empty")
    return sum(nums) / len(nums)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
