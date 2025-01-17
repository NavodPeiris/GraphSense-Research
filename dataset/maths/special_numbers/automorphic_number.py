




def is_automorphic_number(number: int) -> bool:
    if not isinstance(number, int):
        msg = f"Input value of [number={number}] must be an integer"
        raise TypeError(msg)
    if number < 0:
        return False
    number_square = number * number
    while number > 0:
        if number % 10 != number_square % 10:
            return False
        number //= 10
        number_square //= 10
    return True


if __name__ == "__main__":
    import doctest

    doctest.testmod()
