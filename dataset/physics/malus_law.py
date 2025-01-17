import math



def malus_law(initial_intensity: float, angle: float) -> float:

    if initial_intensity < 0:
        raise ValueError("The value of intensity cannot be negative")
        
    if angle < 0 or angle > 360:
        raise ValueError("In Malus Law, the angle is in the range 0-360 degrees")
        
    return initial_intensity * (math.cos(math.radians(angle)) ** 2)


if __name__ == "__main__":
    import doctest

    doctest.testmod(name="malus_law")
