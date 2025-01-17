
from collections.abc import Callable
from math import sqrt

import numpy as np


def runge_kutta_gills(
    func: Callable[[float, float], float],
    x_initial: float,
    y_initial: float,
    step_size: float,
    x_final: float,
) -> np.ndarray:
    if x_initial >= x_final:
        raise ValueError(
            "The final value of x must be greater than initial value of x."
        )

    if step_size <= 0:
        raise ValueError("Step size must be positive.")

    n = int((x_final - x_initial) / step_size)
    y = np.zeros(n + 1)
    y[0] = y_initial
    for i in range(n):
        k1 = step_size * func(x_initial, y[i])
        k2 = step_size * func(x_initial + step_size / 2, y[i] + k1 / 2)
        k3 = step_size * func(
            x_initial + step_size / 2,
            y[i] + (-0.5 + 1 / sqrt(2)) * k1 + (1 - 1 / sqrt(2)) * k2,
        )
        k4 = step_size * func(
            x_initial + step_size, y[i] - (1 / sqrt(2)) * k2 + (1 + 1 / sqrt(2)) * k3
        )

        y[i + 1] = y[i] + (k1 + (2 - sqrt(2)) * k2 + (2 + sqrt(2)) * k3 + k4) / 6
        x_initial += step_size
    return y


if __name__ == "__main__":
    import doctest

    doctest.testmod()
