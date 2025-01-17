
from maths.prime_check import is_prime


def is_germain_prime(number: int) -> bool:
    if not isinstance(number, int) or number < 1:
        msg = f"Input value must be a positive integer. Input value: {number}"
        raise TypeError(msg)

    return is_prime(number) and is_prime(2 * number + 1)


def is_safe_prime(number: int) -> bool:
    if not isinstance(number, int) or number < 1:
        msg = f"Input value must be a positive integer. Input value: {number}"
        raise TypeError(msg)

    return (number - 1) % 2 == 0 and is_prime(number) and is_prime((number - 1) // 2)


if __name__ == "__main__":
    from doctest import testmod

    testmod()
