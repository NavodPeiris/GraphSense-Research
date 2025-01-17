
import numpy as np


def sigmoid(vector: np.ndarray) -> np.ndarray:
    return 1 / (1 + np.exp(-vector))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
