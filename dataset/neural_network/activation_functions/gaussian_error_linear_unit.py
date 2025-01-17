
import numpy as np


def sigmoid(vector: np.ndarray) -> np.ndarray:
    return 1 / (1 + np.exp(-vector))


def gaussian_error_linear_unit(vector: np.ndarray) -> np.ndarray:
    return vector * sigmoid(1.702 * vector)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
