
from math import factorial, pi


def maclaurin_sin(theta: float, accuracy: int = 30) -> float:

    if not isinstance(theta, (int, float)):
        raise ValueError("maclaurin_sin() requires either an int or float for theta")

    if not isinstance(accuracy, int) or accuracy <= 0:
        raise ValueError("maclaurin_sin() requires a positive int for accuracy")

    theta = float(theta)
    div = theta // (2 * pi)
    theta -= 2 * div * pi
    return sum(
        (-1) ** r * theta ** (2 * r + 1) / factorial(2 * r + 1) for r in range(accuracy)
    )


def maclaurin_cos(theta: float, accuracy: int = 30) -> float:

    if not isinstance(theta, (int, float)):
        raise ValueError("maclaurin_cos() requires either an int or float for theta")

    if not isinstance(accuracy, int) or accuracy <= 0:
        raise ValueError("maclaurin_cos() requires a positive int for accuracy")

    theta = float(theta)
    div = theta // (2 * pi)
    theta -= 2 * div * pi
    return sum((-1) ** r * theta ** (2 * r) / factorial(2 * r) for r in range(accuracy))


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print(maclaurin_sin(10))
    print(maclaurin_sin(-10))
    print(maclaurin_sin(10, 15))
    print(maclaurin_sin(-10, 15))

    print(maclaurin_cos(5))
    print(maclaurin_cos(-5))
    print(maclaurin_cos(10, 15))
    print(maclaurin_cos(-10, 15))
