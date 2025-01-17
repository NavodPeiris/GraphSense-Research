
from scipy.constants import c  


def energy_from_mass(mass: float) -> float:
    if mass < 0:
        raise ValueError("Mass can't be negative.")
    return mass * c**2


def mass_from_energy(energy: float) -> float:
    if energy < 0:
        raise ValueError("Energy can't be negative.")
    return energy / c**2


if __name__ == "__main__":
    import doctest

    doctest.testmod()
