import math


def real_power(apparent_power: float, power_factor: float) -> float:
    if (
        not isinstance(power_factor, (int, float))
        or power_factor < -1
        or power_factor > 1
    ):
        raise ValueError("power_factor must be a valid float value between -1 and 1.")
    return apparent_power * power_factor


def reactive_power(apparent_power: float, power_factor: float) -> float:
    if (
        not isinstance(power_factor, (int, float))
        or power_factor < -1
        or power_factor > 1
    ):
        raise ValueError("power_factor must be a valid float value between -1 and 1.")
    return apparent_power * math.sqrt(1 - power_factor**2)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
