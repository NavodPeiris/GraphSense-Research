from __future__ import annotations



def shear_stress(
    stress: float,
    tangential_force: float,
    area: float,
) -> tuple[str, float]:
    if (stress, tangential_force, area).count(0) != 1:
        raise ValueError("You cannot supply more or less than 2 values")
    elif stress < 0:
        raise ValueError("Stress cannot be negative")
    elif tangential_force < 0:
        raise ValueError("Tangential Force cannot be negative")
    elif area < 0:
        raise ValueError("Area cannot be negative")
    elif stress == 0:
        return (
            "stress",
            tangential_force / area,
        )
    elif tangential_force == 0:
        return (
            "tangential_force",
            stress * area,
        )
    else:
        return (
            "area",
            tangential_force / stress,
        )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
