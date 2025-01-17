
import warnings
from collections.abc import Callable
from typing import Any

import matplotlib.pyplot as plt
import numpy as np

c_cauliflower = 0.25 + 0.0j
c_polynomial_1 = -0.4 + 0.6j
c_polynomial_2 = -0.1 + 0.651j
c_exponential = -2.0
nb_iterations = 56
window_size = 2.0
nb_pixels = 666


def eval_exponential(c_parameter: complex, z_values: np.ndarray) -> np.ndarray:
    return np.exp(z_values) + c_parameter


def eval_quadratic_polynomial(c_parameter: complex, z_values: np.ndarray) -> np.ndarray:
    return z_values * z_values + c_parameter


def prepare_grid(window_size: float, nb_pixels: int) -> np.ndarray:
    x = np.linspace(-window_size, window_size, nb_pixels)
    x = x.reshape((nb_pixels, 1))
    y = np.linspace(-window_size, window_size, nb_pixels)
    y = y.reshape((1, nb_pixels))
    return x + 1.0j * y


def iterate_function(
    eval_function: Callable[[Any, np.ndarray], np.ndarray],
    function_params: Any,
    nb_iterations: int,
    z_0: np.ndarray,
    infinity: float | None = None,
) -> np.ndarray:

    z_n = z_0.astype("complex64")
    for _ in range(nb_iterations):
        z_n = eval_function(function_params, z_n)
        if infinity is not None:
            np.nan_to_num(z_n, copy=False, nan=infinity)
            z_n[abs(z_n) == np.inf] = infinity
    return z_n


def show_results(
    function_label: str,
    function_params: Any,
    escape_radius: float,
    z_final: np.ndarray,
) -> None:

    abs_z_final = (abs(z_final)).transpose()
    abs_z_final[:, :] = abs_z_final[::-1, :]
    plt.matshow(abs_z_final < escape_radius)
    plt.title(f"Julia set of ${function_label}$, $c={function_params}$")
    plt.show()


def ignore_overflow_warnings() -> None:
    warnings.filterwarnings(
        "ignore", category=RuntimeWarning, message="overflow encountered in multiply"
    )
    warnings.filterwarnings(
        "ignore",
        category=RuntimeWarning,
        message="invalid value encountered in multiply",
    )
    warnings.filterwarnings(
        "ignore", category=RuntimeWarning, message="overflow encountered in absolute"
    )
    warnings.filterwarnings(
        "ignore", category=RuntimeWarning, message="overflow encountered in exp"
    )


if __name__ == "__main__":
    z_0 = prepare_grid(window_size, nb_pixels)

    ignore_overflow_warnings()  

    nb_iterations = 24
    escape_radius = 2 * abs(c_cauliflower) + 1
    z_final = iterate_function(
        eval_quadratic_polynomial,
        c_cauliflower,
        nb_iterations,
        z_0,
        infinity=1.1 * escape_radius,
    )
    show_results("z^2+c", c_cauliflower, escape_radius, z_final)

    nb_iterations = 64
    escape_radius = 2 * abs(c_polynomial_1) + 1
    z_final = iterate_function(
        eval_quadratic_polynomial,
        c_polynomial_1,
        nb_iterations,
        z_0,
        infinity=1.1 * escape_radius,
    )
    show_results("z^2+c", c_polynomial_1, escape_radius, z_final)

    nb_iterations = 161
    escape_radius = 2 * abs(c_polynomial_2) + 1
    z_final = iterate_function(
        eval_quadratic_polynomial,
        c_polynomial_2,
        nb_iterations,
        z_0,
        infinity=1.1 * escape_radius,
    )
    show_results("z^2+c", c_polynomial_2, escape_radius, z_final)

    nb_iterations = 12
    escape_radius = 10000.0
    z_final = iterate_function(
        eval_exponential,
        c_exponential,
        nb_iterations,
        z_0 + 2,
        infinity=1.0e10,
    )
    show_results("e^z+c", c_exponential, escape_radius, z_final)
