
import numpy as np


def exponential_linear_unit(vector: np.ndarray, alpha: float) -> np.ndarray:
    return np.where(vector > 0, vector, (alpha * (np.exp(vector) - 1)))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
