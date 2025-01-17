
from __future__ import annotations

import numpy as np


def relu(vector: list[float]):

    
    return np.maximum(0, vector)


if __name__ == "__main__":
    print(np.array(relu([-1, 0, 5])))
