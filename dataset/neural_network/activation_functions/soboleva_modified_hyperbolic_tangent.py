
import numpy as np


def soboleva_modified_hyperbolic_tangent(
    vector: np.ndarray, a_value: float, b_value: float, c_value: float, d_value: float
) -> np.ndarray:

    
    
    numerator = np.exp(a_value * vector) - np.exp(-b_value * vector)
    denominator = np.exp(c_value * vector) + np.exp(-d_value * vector)

    
    return numerator / denominator


if __name__ == "__main__":
    import doctest

    doctest.testmod()
