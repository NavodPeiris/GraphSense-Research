
import numpy as np

from .softplus import softplus


def mish(vector: np.ndarray) -> np.ndarray:
    return vector * np.tanh(softplus(vector))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
