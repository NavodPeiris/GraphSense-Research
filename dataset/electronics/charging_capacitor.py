



from math import exp  


def charging_capacitor(
    source_voltage: float,  
    resistance: float,  
    capacitance: float,  
    time_sec: float,  
) -> float:

    if source_voltage <= 0:
        raise ValueError("Source voltage must be positive.")
    if resistance <= 0:
        raise ValueError("Resistance must be positive.")
    if capacitance <= 0:
        raise ValueError("Capacitance must be positive.")
    return round(source_voltage * (1 - exp(-time_sec / (resistance * capacitance))), 3)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
