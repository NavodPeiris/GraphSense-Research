def perfect_cube(n: int) -> bool:
    val = n ** (1 / 3)
    return (val * val * val) == n


def perfect_cube_binary_search(n: int) -> bool:
    if not isinstance(n, int):
        raise TypeError("perfect_cube_binary_search() only accepts integers")
    if n < 0:
        n = -n
    left = 0
    right = n
    while left <= right:
        mid = left + (right - left) // 2
        if mid * mid * mid == n:
            return True
        elif mid * mid * mid < n:
            left = mid + 1
        else:
            right = mid - 1
    return False


if __name__ == "__main__":
    import doctest

    doctest.testmod()
