
import numpy as np


def leaky_rectified_linear_unit(vector: np.ndarray, alpha: float) -> np.ndarray:
    return np.where(vector > 0, vector, alpha * vector)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
