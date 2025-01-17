

def integer_square_root(num: int) -> int:
    if not isinstance(num, int) or num < 0:
        raise ValueError("num must be non-negative integer")

    if num < 2:
        return num

    left_bound = 0
    right_bound = num // 2

    while left_bound <= right_bound:
        mid = left_bound + (right_bound - left_bound) // 2
        mid_squared = mid * mid
        if mid_squared == num:
            return mid

        if mid_squared < num:
            left_bound = mid + 1
        else:
            right_bound = mid - 1

    return right_bound


if __name__ == "__main__":
    import doctest

    doctest.testmod()
