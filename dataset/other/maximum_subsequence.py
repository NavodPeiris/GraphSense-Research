from collections.abc import Sequence


def max_subsequence_sum(nums: Sequence[int] | None = None) -> int:
    if nums is None or not nums:
        raise ValueError("Input sequence should not be empty")

    ans = nums[0]
    for i in range(1, len(nums)):
        num = nums[i]
        ans = max(ans, ans + num, num)

    return ans


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    
    n = int(input("Enter number of elements : ").strip())
    array = list(map(int, input("\nEnter the numbers : ").strip().split()))[:n]
    print(max_subsequence_sum(array))
