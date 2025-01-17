

def int_to_base(number: int, base: int) -> str:

    if base < 2 or base > 36:
        raise ValueError("'base' must be between 2 and 36 inclusive")

    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    if number < 0:
        raise ValueError("number must be a positive integer")

    while number > 0:
        number, remainder = divmod(number, base)
        result = digits[remainder] + result

    if result == "":
        result = "0"

    return result


def sum_of_digits(num: int, base: int) -> str:

    if base < 2 or base > 36:
        raise ValueError("'base' must be between 2 and 36 inclusive")

    num_str = int_to_base(num, base)
    res = sum(int(char, base) for char in num_str)
    res_str = int_to_base(res, base)
    return res_str


def harshad_numbers_in_base(limit: int, base: int) -> list[str]:

    if base < 2 or base > 36:
        raise ValueError("'base' must be between 2 and 36 inclusive")

    if limit < 0:
        return []

    numbers = [
        int_to_base(i, base)
        for i in range(1, limit)
        if i % int(sum_of_digits(i, base), base) == 0
    ]

    return numbers


def is_harshad_number_in_base(num: int, base: int) -> bool:

    if base < 2 or base > 36:
        raise ValueError("'base' must be between 2 and 36 inclusive")

    if num < 0:
        return False

    n = int_to_base(num, base)
    d = sum_of_digits(num, base)
    return int(n, base) % int(d, base) == 0


if __name__ == "__main__":
    import doctest

    doctest.testmod()
