

def kinetic_energy(mass: float, velocity: float) -> float:
    if mass < 0:
        raise ValueError("The mass of a body cannot be negative")
    return 0.5 * mass * abs(velocity) * abs(velocity)


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
