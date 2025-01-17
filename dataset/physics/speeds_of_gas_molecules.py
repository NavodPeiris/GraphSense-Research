

from scipy.constants import R, pi


def avg_speed_of_molecule(temperature: float, molar_mass: float) -> float:

    if temperature < 0:
        raise Exception("Absolute temperature cannot be less than 0 K")
    if molar_mass <= 0:
        raise Exception("Molar mass should be greater than 0 kg/mol")
    return (8 * R * temperature / (pi * molar_mass)) ** 0.5


def mps_speed_of_molecule(temperature: float, molar_mass: float) -> float:

    if temperature < 0:
        raise Exception("Absolute temperature cannot be less than 0 K")
    if molar_mass <= 0:
        raise Exception("Molar mass should be greater than 0 kg/mol")
    return (2 * R * temperature / molar_mass) ** 0.5


if __name__ == "__main__":
    import doctest

    doctest.testmod()
