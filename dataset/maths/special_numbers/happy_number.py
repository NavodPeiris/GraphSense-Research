def is_happy_number(number: int) -> bool:
    if not isinstance(number, int) or number <= 0:
        msg = f"{number=} must be a positive integer"
        raise ValueError(msg)

    seen = set()
    while number != 1 and number not in seen:
        seen.add(number)
        number = sum(int(digit) ** 2 for digit in str(number))
    return number == 1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
