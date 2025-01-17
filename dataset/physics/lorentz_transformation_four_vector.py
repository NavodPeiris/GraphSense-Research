
from math import sqrt

import numpy as np
from sympy import symbols



c = 299792458


ct, x, y, z = symbols("ct x y z")



def beta(velocity: float) -> float:
    if velocity > c:
        raise ValueError("Speed must not exceed light speed 299,792,458 [m/s]!")
    elif velocity < 1:
        
        raise ValueError("Speed must be greater than or equal to 1!")

    return velocity / c


def gamma(velocity: float) -> float:
    return 1 / sqrt(1 - beta(velocity) ** 2)


def transformation_matrix(velocity: float) -> np.ndarray:
    return np.array(
        [
            [gamma(velocity), -gamma(velocity) * beta(velocity), 0, 0],
            [-gamma(velocity) * beta(velocity), gamma(velocity), 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1],
        ]
    )


def transform(velocity: float, event: np.ndarray | None = None) -> np.ndarray:
    
    if event is None:
        event = np.array([ct, x, y, z])  
    else:
        event[0] *= c  

    return transformation_matrix(velocity) @ event


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    
    four_vector = transform(29979245)
    print("Example of four vector: ")
    print(f"ct' = {four_vector[0]}")
    print(f"x' = {four_vector[1]}")
    print(f"y' = {four_vector[2]}")
    print(f"z' = {four_vector[3]}")

    
    sub_dict = {ct: c, x: 1, y: 1, z: 1}
    numerical_vector = [four_vector[i].subs(sub_dict) for i in range(4)]

    print(f"\n{numerical_vector}")
