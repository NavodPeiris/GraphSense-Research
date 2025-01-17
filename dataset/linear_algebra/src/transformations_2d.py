
from math import cos, sin


def scaling(scaling_factor: float) -> list[list[float]]:
    scaling_factor = float(scaling_factor)
    return [[scaling_factor * int(x == y) for x in range(2)] for y in range(2)]


def rotation(angle: float) -> list[list[float]]:
    c, s = cos(angle), sin(angle)
    return [[c, -s], [s, c]]


def projection(angle: float) -> list[list[float]]:
    c, s = cos(angle), sin(angle)
    cs = c * s
    return [[c * c, cs], [cs, s * s]]


def reflection(angle: float) -> list[list[float]]:
    c, s = cos(angle), sin(angle)
    cs = c * s
    return [[2 * c - 1, 2 * cs], [2 * cs, 2 * s - 1]]


print(f"    {scaling(5) = }")
print(f"  {rotation(45) = }")
print(f"{projection(45) = }")
print(f"{reflection(45) = }")
