
import numpy as np


def tangent_hyperbolic(vector: np.ndarray) -> np.ndarray:

    return (2 / (1 + np.exp(-2 * vector))) - 1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
