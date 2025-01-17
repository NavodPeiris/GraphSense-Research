



from math import exp  


def charging_inductor(
    source_voltage: float,  
    resistance: float,  
    inductance: float,  
    time: float,  
) -> float:

    if source_voltage <= 0:
        raise ValueError("Source voltage must be positive.")
    if resistance <= 0:
        raise ValueError("Resistance must be positive.")
    if inductance <= 0:
        raise ValueError("Inductance must be positive.")
    return round(
        source_voltage / resistance * (1 - exp((-time * resistance) / inductance)), 3
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
