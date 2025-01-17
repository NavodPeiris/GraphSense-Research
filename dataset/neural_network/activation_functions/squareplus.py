
import numpy as np


def squareplus(vector: np.ndarray, beta: float) -> np.ndarray:
    return (vector + np.sqrt(vector**2 + beta)) / 2


if __name__ == "__main__":
    import doctest

    doctest.testmod()
