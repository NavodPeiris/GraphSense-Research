

ENERGY_CONVERSION: dict[str, float] = {
    "joule": 1.0,
    "kilojoule": 1_000,
    "megajoule": 1_000_000,
    "gigajoule": 1_000_000_000,
    "wattsecond": 1.0,
    "watthour": 3_600,
    "kilowatthour": 3_600_000,
    "newtonmeter": 1.0,
    "calorie_nutr": 4_186.8,
    "kilocalorie_nutr": 4_186_800.00,
    "electronvolt": 1.602_176_634e-19,
    "britishthermalunit_it": 1_055.055_85,
    "footpound": 1.355_818,
}


def energy_conversion(from_type: str, to_type: str, value: float) -> float:
    
    if to_type not in ENERGY_CONVERSION or from_type not in ENERGY_CONVERSION:
        msg = (
            f"Incorrect 'from_type' or 'to_type' value: {from_type!r}, {to_type!r}\n"
            f"Valid values are: {', '.join(ENERGY_CONVERSION)}"
        )
        raise ValueError(msg)
    return value * ENERGY_CONVERSION[from_type] / ENERGY_CONVERSION[to_type]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
