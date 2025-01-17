

def reynolds_number(
    density: float, velocity: float, diameter: float, viscosity: float
) -> float:

    if density <= 0 or diameter <= 0 or viscosity <= 0:
        raise ValueError(
            "please ensure that density, diameter and viscosity are positive"
        )
    return (density * abs(velocity) * diameter) / viscosity


if __name__ == "__main__":
    import doctest

    doctest.testmod()
