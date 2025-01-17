
import math

from numpy import inf
from scipy.integrate import quad


def gamma_iterative(num: float) -> float:
    if num <= 0:
        raise ValueError("math domain error")

    return quad(integrand, 0, inf, args=(num))[0]


def integrand(x: float, z: float) -> float:
    return math.pow(x, z - 1) * math.exp(-x)


def gamma_recursive(num: float) -> float:
    if num <= 0:
        raise ValueError("math domain error")
    if num > 171.5:
        raise OverflowError("math range error")
    elif num - int(num) not in (0, 0.5):
        raise NotImplementedError("num must be an integer or a half-integer")
    elif num == 0.5:
        return math.sqrt(math.pi)
    else:
        return 1.0 if num == 1 else (num - 1) * gamma_recursive(num - 1)


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    num = 1.0
    while num:
        num = float(input("Gamma of: "))
        print(f"gamma_iterative({num}) = {gamma_iterative(num)}")
        print(f"gamma_recursive({num}) = {gamma_recursive(num)}")
        print("\nEnter 0 to exit...")
