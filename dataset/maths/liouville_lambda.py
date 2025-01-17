

from maths.prime_factors import prime_factors


def liouville_lambda(number: int) -> int:
    if not isinstance(number, int):
        msg = f"Input value of [number={number}] must be an integer"
        raise TypeError(msg)
    if number < 1:
        raise ValueError("Input must be a positive integer")
    return -1 if len(prime_factors(number)) % 2 else 1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
