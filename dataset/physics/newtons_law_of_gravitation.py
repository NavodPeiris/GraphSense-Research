
from __future__ import annotations


GRAVITATIONAL_CONSTANT = 6.6743e-11  


def gravitational_law(
    force: float, mass_1: float, mass_2: float, distance: float
) -> dict[str, float]:

    product_of_mass = mass_1 * mass_2

    if (force, mass_1, mass_2, distance).count(0) != 1:
        raise ValueError("One and only one argument must be 0")
    if force < 0:
        raise ValueError("Gravitational force can not be negative")
    if distance < 0:
        raise ValueError("Distance can not be negative")
    if mass_1 < 0 or mass_2 < 0:
        raise ValueError("Mass can not be negative")
    if force == 0:
        force = GRAVITATIONAL_CONSTANT * product_of_mass / (distance**2)
        return {"force": force}
    elif mass_1 == 0:
        mass_1 = (force) * (distance**2) / (GRAVITATIONAL_CONSTANT * mass_2)
        return {"mass_1": mass_1}
    elif mass_2 == 0:
        mass_2 = (force) * (distance**2) / (GRAVITATIONAL_CONSTANT * mass_1)
        return {"mass_2": mass_2}
    elif distance == 0:
        distance = (GRAVITATIONAL_CONSTANT * product_of_mass / (force)) ** 0.5
        return {"distance": distance}
    raise ValueError("One and only one argument must be 0")



if __name__ == "__main__":
    import doctest

    doctest.testmod()
