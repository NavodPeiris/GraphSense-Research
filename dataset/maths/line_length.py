from __future__ import annotations

import math
from collections.abc import Callable


def line_length(
    fnc: Callable[[float], float],
    x_start: float,
    x_end: float,
    steps: int = 100,
) -> float:

    x1 = x_start
    fx1 = fnc(x_start)
    length = 0.0

    for _ in range(steps):
        
        x2 = (x_end - x_start) / steps + x1
        fx2 = fnc(x2)
        length += math.hypot(x2 - x1, fx2 - fx1)

        
        x1 = x2
        fx1 = fx2

    return length


if __name__ == "__main__":

    def f(x):
        return math.sin(10 * x)

    print("f(x) = sin(10 * x)")
    print("The length of the curve from x = -10 to x = 10 is:")
    i = 10
    while i <= 100000:
        print(f"With {i} steps: {line_length(f, -10, 10, i)}")
        i *= 10
