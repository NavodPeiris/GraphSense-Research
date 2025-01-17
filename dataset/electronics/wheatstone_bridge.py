
from __future__ import annotations


def wheatstone_solver(
    resistance_1: float, resistance_2: float, resistance_3: float
) -> float:

    if resistance_1 <= 0 or resistance_2 <= 0 or resistance_3 <= 0:
        raise ValueError("All resistance values must be positive")
    else:
        return float((resistance_2 / resistance_1) * resistance_3)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
