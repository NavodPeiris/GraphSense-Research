
UNIVERSAL_GAS_CONSTANT = 8.3144598


def rms_speed_of_molecule(temperature: float, molar_mass: float) -> float:
    if temperature < 0:
        raise Exception("Temperature cannot be less than 0 K")
    if molar_mass <= 0:
        raise Exception("Molar mass cannot be less than or equal to 0 kg/mol")
    else:
        return (3 * UNIVERSAL_GAS_CONSTANT * temperature / molar_mass) ** 0.5


if __name__ == "__main__":
    import doctest

    
    doctest.testmod()

    
    temperature = 300
    molar_mass = 28
    vrms = rms_speed_of_molecule(temperature, molar_mass)
    print(f"Vrms of Nitrogen gas at 300 K is {vrms} m/s")
