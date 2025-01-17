from collections.abc import Sequence


def evaluate_poly(poly: Sequence[float], x: float) -> float:
    return sum(c * (x**i) for i, c in enumerate(poly))


def horner(poly: Sequence[float], x: float) -> float:
    result = 0.0
    for coeff in reversed(poly):
        result = result * x + coeff
    return result


if __name__ == "__main__":
    poly = (0.0, 0.0, 5.0, 9.3, 7.0)
    x = 10.0
    print(evaluate_poly(poly, x))
    print(horner(poly, x))
