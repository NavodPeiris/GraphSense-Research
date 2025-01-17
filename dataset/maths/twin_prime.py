

from maths.prime_check import is_prime


def twin_prime(number: int) -> int:
    if not isinstance(number, int):
        msg = f"Input value of [number={number}] must be an integer"
        raise TypeError(msg)
    if is_prime(number) and is_prime(number + 2):
        return number + 2
    else:
        return -1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
