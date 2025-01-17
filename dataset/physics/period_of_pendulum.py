
from math import pi

from scipy.constants import g


def period_of_pendulum(length: float) -> float:
    if length < 0:
        raise ValueError("The length should be non-negative")
    return 2 * pi * (length / g) ** 0.5


if __name__ == "__main__":
    import doctest

    doctest.testmod()
