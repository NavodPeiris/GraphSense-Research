from collections.abc import Callable

import numpy as np


def euler_modified(
    ode_func: Callable, y0: float, x0: float, step_size: float, x_end: float
) -> np.ndarray:
    n = int(np.ceil((x_end - x0) / step_size))
    y = np.zeros((n + 1,))
    y[0] = y0
    x = x0

    for k in range(n):
        y_get = y[k] + step_size * ode_func(x, y[k])
        y[k + 1] = y[k] + (
            (step_size / 2) * (ode_func(x, y[k]) + ode_func(x + step_size, y_get))
        )
        x += step_size

    return y


if __name__ == "__main__":
    import doctest

    doctest.testmod()
