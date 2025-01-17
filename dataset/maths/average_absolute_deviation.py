def average_absolute_deviation(nums: list[int]) -> float:
    if not nums:  
        raise ValueError("List is empty")

    average = sum(nums) / len(nums)  
    return sum(abs(x - average) for x in nums) / len(nums)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
