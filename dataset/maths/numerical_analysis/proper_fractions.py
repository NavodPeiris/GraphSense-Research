from math import gcd


def proper_fractions(denominator: int) -> list[str]:

    if denominator < 0:
        raise ValueError("The Denominator Cannot be less than 0")
    elif isinstance(denominator, float):
        raise ValueError("The Denominator must be an integer")
    return [
        f"{numerator}/{denominator}"
        for numerator in range(1, denominator)
        if gcd(numerator, denominator) == 1
    ]


if __name__ == "__main__":
    from doctest import testmod

    testmod()
