def is_int_palindrome(num: int) -> bool:
    if num < 0:
        return False

    num_copy: int = num
    rev_num: int = 0
    while num > 0:
        rev_num = rev_num * 10 + (num % 10)
        num //= 10

    return num_copy == rev_num


if __name__ == "__main__":
    import doctest

    doctest.testmod()
