
from numpy import exp, pi, sqrt


def gaussian(x, mu: float = 0.0, sigma: float = 1.0) -> float:
    return 1 / sqrt(2 * pi * sigma**2) * exp(-((x - mu) ** 2) / (2 * sigma**2))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
