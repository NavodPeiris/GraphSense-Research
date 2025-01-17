
import numpy as np


def sigmoid(vector: np.ndarray) -> np.ndarray:
    return 1 / (1 + np.exp(-vector))


def sigmoid_linear_unit(vector: np.ndarray) -> np.ndarray:
    return vector * sigmoid(vector)


def swish(vector: np.ndarray, trainable_parameter: int) -> np.ndarray:
    return vector * sigmoid(trainable_parameter * vector)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
