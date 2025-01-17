
import numpy as np


def binary_step(vector: np.ndarray) -> np.ndarray:

    return np.where(vector >= 0, 1, 0)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
