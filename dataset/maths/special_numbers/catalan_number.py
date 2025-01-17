

def catalan(number: int) -> int:

    if not isinstance(number, int):
        msg = f"Input value of [number={number}] must be an integer"
        raise TypeError(msg)

    if number < 1:
        msg = f"Input value of [number={number}] must be > 0"
        raise ValueError(msg)

    current_number = 1

    for i in range(1, number):
        current_number *= 4 * i - 2
        current_number //= i + 1

    return current_number


if __name__ == "__main__":
    import doctest

    doctest.testmod()
