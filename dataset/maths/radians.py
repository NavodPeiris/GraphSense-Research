from math import pi


def radians(degree: float) -> float:

    return degree / (180 / pi)


if __name__ == "__main__":
    from doctest import testmod

    testmod()
