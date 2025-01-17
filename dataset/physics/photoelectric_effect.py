
PLANCK_CONSTANT_JS = 6.6261 * pow(10, -34)  
PLANCK_CONSTANT_EVS = 4.1357 * pow(10, -15)  


def maximum_kinetic_energy(
    frequency: float, work_function: float, in_ev: bool = False
) -> float:
    if frequency < 0:
        raise ValueError("Frequency can't be negative.")
    if in_ev:
        return max(PLANCK_CONSTANT_EVS * frequency - work_function, 0)
    return max(PLANCK_CONSTANT_JS * frequency - work_function, 0)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
