import cmath
import math


def apparent_power(
    voltage: float, current: float, voltage_angle: float, current_angle: float
) -> complex:
    
    voltage_angle_rad = math.radians(voltage_angle)
    current_angle_rad = math.radians(current_angle)

    
    voltage_rect = cmath.rect(voltage, voltage_angle_rad)
    current_rect = cmath.rect(current, current_angle_rad)

    
    return voltage_rect * current_rect


if __name__ == "__main__":
    import doctest

    doctest.testmod()
