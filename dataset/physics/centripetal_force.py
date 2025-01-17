

def centripetal(mass: float, velocity: float, radius: float) -> float:
    if mass < 0:
        raise ValueError("The mass of the body cannot be negative")
    if radius <= 0:
        raise ValueError("The radius is always a positive non zero integer")
    return (mass * (velocity) ** 2) / radius


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
