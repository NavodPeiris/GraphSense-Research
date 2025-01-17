import math


def perfect_square(num: int) -> bool:
    return math.sqrt(num) * math.sqrt(num) == num


def perfect_square_binary_search(n: int) -> bool:
    left = 0
    right = n
    while left <= right:
        mid = (left + right) // 2
        if mid**2 == n:
            return True
        elif mid**2 > n:
            right = mid - 1
        else:
            left = mid + 1
    return False


if __name__ == "__main__":
    import doctest

    doctest.testmod()
