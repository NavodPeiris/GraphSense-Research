
from collections.abc import Callable

import numpy as np


def runge_kutta_fehlberg_45(
    func: Callable,
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
    y = np.zeros(
        (n + 1),
    )
    x = np.zeros(n + 1)
    y[0] = y_initial
    x[0] = x_initial
    for i in range(n):
        k1 = step_size * func(x[i], y[i])
        k2 = step_size * func(x[i] + step_size / 4, y[i] + k1 / 4)
        k3 = step_size * func(
            x[i] + (3 / 8) * step_size, y[i] + (3 / 32) * k1 + (9 / 32) * k2
        )
        k4 = step_size * func(
            x[i] + (12 / 13) * step_size,
            y[i] + (1932 / 2197) * k1 - (7200 / 2197) * k2 + (7296 / 2197) * k3,
        )
        k5 = step_size * func(
            x[i] + step_size,
            y[i] + (439 / 216) * k1 - 8 * k2 + (3680 / 513) * k3 - (845 / 4104) * k4,
        )
        k6 = step_size * func(
            x[i] + step_size / 2,
            y[i]
            - (8 / 27) * k1
            + 2 * k2
            - (3544 / 2565) * k3
            + (1859 / 4104) * k4
            - (11 / 40) * k5,
        )
        y[i + 1] = (
            y[i]
            + (16 / 135) * k1
            + (6656 / 12825) * k3
            + (28561 / 56430) * k4
            - (9 / 50) * k5
            + (2 / 55) * k6
        )
        x[i + 1] = step_size + x[i]
    return y


if __name__ == "__main__":
    import doctest

    doctest.testmod()
