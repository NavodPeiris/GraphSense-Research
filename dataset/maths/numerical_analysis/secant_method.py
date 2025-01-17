
from math import exp


def f(x: float) -> float:
    return 8 * x - 2 * exp(-x)


def secant_method(lower_bound: float, upper_bound: float, repeats: int) -> float:
    x0 = lower_bound
    x1 = upper_bound
    for _ in range(repeats):
        x0, x1 = x1, x1 - (f(x1) * (x1 - x0)) / (f(x1) - f(x0))
    return x1


if __name__ == "__main__":
    print(f"Example: {secant_method(1, 3, 2)}")
