
from fractions import Fraction
from math import floor


def continued_fraction(num: Fraction) -> list[int]:
    numerator, denominator = num.as_integer_ratio()
    continued_fraction_list: list[int] = []
    while True:
        integer_part = floor(numerator / denominator)
        continued_fraction_list.append(integer_part)
        numerator -= integer_part * denominator
        if numerator == 0:
            break
        numerator, denominator = denominator, numerator

    return continued_fraction_list


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print("Continued Fraction of 0.84375 is: ", continued_fraction(Fraction("0.84375")))
