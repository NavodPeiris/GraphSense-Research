

def molarity_to_normality(nfactor: int, moles: float, volume: float) -> float:
    
    return round(float(moles / volume) * nfactor)


def moles_to_pressure(volume: float, moles: float, temperature: float) -> float:
    
    return round(float((moles * 0.0821 * temperature) / (volume)))


def moles_to_volume(pressure: float, moles: float, temperature: float) -> float:
   
    return round(float((moles * 0.0821 * temperature) / (pressure)))


def pressure_and_volume_to_temperature(
    pressure: float, moles: float, volume: float
) -> float:
    
    return round(float((pressure * volume) / (0.0821 * moles)))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
