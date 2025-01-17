
from maths.is_square_free import is_square_free
from maths.prime_factors import prime_factors


def mobius(n: int) -> int:
    factors = prime_factors(n)
    if is_square_free(factors):
        return -1 if len(factors) % 2 else 1
    return 0


if __name__ == "__main__":
    import doctest

    doctest.testmod()
