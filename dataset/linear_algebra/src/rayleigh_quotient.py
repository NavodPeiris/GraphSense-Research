
from typing import Any

import numpy as np


def is_hermitian(matrix: np.ndarray) -> bool:
    return np.array_equal(matrix, matrix.conjugate().T)


def rayleigh_quotient(a: np.ndarray, v: np.ndarray) -> Any:
    v_star = v.conjugate().T
    v_star_dot = v_star.dot(a)
    assert isinstance(v_star_dot, np.ndarray)
    return (v_star_dot.dot(v)) / (v_star.dot(v))


def tests() -> None:
    a = np.array([[2, 2 + 1j, 4], [2 - 1j, 3, 1j], [4, -1j, 1]])
    v = np.array([[1], [2], [3]])
    assert is_hermitian(a), f"{a} is not hermitian."
    print(rayleigh_quotient(a, v))

    a = np.array([[1, 2, 4], [2, 3, -1], [4, -1, 1]])
    assert is_hermitian(a), f"{a} is not hermitian."
    assert rayleigh_quotient(a, v) == float(3)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    tests()
