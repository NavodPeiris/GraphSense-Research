
def is_monotonic(nums: list[int]) -> bool:
    
    return all(nums[i] <= nums[i + 1] for i in range(len(nums) - 1)) or all(
        nums[i] >= nums[i + 1] for i in range(len(nums) - 1)
    )



if __name__ == "__main__":
    
    print(is_monotonic([1, 2, 2, 3]))  
    print(is_monotonic([6, 5, 4, 4]))  
    print(is_monotonic([1, 3, 2]))  

    import doctest

    doctest.testmod()
