

def speed_of_sound_in_a_fluid(density: float, bulk_modulus: float) -> float:

    if density <= 0:
        raise ValueError("Impossible fluid density")
    if bulk_modulus <= 0:
        raise ValueError("Impossible bulk modulus")

    return (bulk_modulus / density) ** 0.5


if __name__ == "__main__":
    import doctest

    doctest.testmod()
