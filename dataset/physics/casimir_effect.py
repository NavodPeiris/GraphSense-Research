
from __future__ import annotations

from math import pi



REDUCED_PLANCK_CONSTANT = 1.054571817e-34  

SPEED_OF_LIGHT = 3e8  


def casimir_force(force: float, area: float, distance: float) -> dict[str, float]:

    if (force, area, distance).count(0) != 1:
        raise ValueError("One and only one argument must be 0")
    if force < 0:
        raise ValueError("Magnitude of force can not be negative")
    if distance < 0:
        raise ValueError("Distance can not be negative")
    if area < 0:
        raise ValueError("Area can not be negative")
    if force == 0:
        force = (REDUCED_PLANCK_CONSTANT * SPEED_OF_LIGHT * pi**2 * area) / (
            240 * (distance) ** 4
        )
        return {"force": force}
    elif area == 0:
        area = (240 * force * (distance) ** 4) / (
            REDUCED_PLANCK_CONSTANT * SPEED_OF_LIGHT * pi**2
        )
        return {"area": area}
    elif distance == 0:
        distance = (
            (REDUCED_PLANCK_CONSTANT * SPEED_OF_LIGHT * pi**2 * area) / (240 * force)
        ) ** (1 / 4)
        return {"distance": distance}
    raise ValueError("One and only one argument must be 0")



if __name__ == "__main__":
    import doctest

    doctest.testmod()
