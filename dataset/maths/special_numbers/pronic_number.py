



def is_pronic(number: int) -> bool:
    if not isinstance(number, int):
        msg = f"Input value of [number={number}] must be an integer"
        raise TypeError(msg)
    if number < 0 or number % 2 == 1:
        return False
    number_sqrt = int(number**0.5)
    return number == number_sqrt * (number_sqrt + 1)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
