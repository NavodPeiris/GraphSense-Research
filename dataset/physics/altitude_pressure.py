

def get_altitude_at_pressure(pressure: float) -> float:

    if pressure > 101325:
        raise ValueError("Value Higher than Pressure at Sea Level !")
    if pressure < 0:
        raise ValueError("Atmospheric Pressure can not be negative !")
    return 44_330 * (1 - (pressure / 101_325) ** (1 / 5.5255))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
