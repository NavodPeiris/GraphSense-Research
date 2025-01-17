
import numpy as np


def softplus(vector: np.ndarray) -> np.ndarray:
    return np.log(1 + np.exp(vector))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
