

def hubble_parameter(
    hubble_constant: float,
    radiation_density: float,
    matter_density: float,
    dark_energy: float,
    redshift: float,
) -> float:
    parameters = [redshift, radiation_density, matter_density, dark_energy]
    if any(p < 0 for p in parameters):
        raise ValueError("All input parameters must be positive")

    if any(p > 1 for p in parameters[1:4]):
        raise ValueError("Relative densities cannot be greater than one")
    else:
        curvature = 1 - (matter_density + radiation_density + dark_energy)

        e_2 = (
            radiation_density * (redshift + 1) ** 4
            + matter_density * (redshift + 1) ** 3
            + curvature * (redshift + 1) ** 2
            + dark_energy
        )

        hubble = hubble_constant * e_2 ** (1 / 2)
        return hubble


if __name__ == "__main__":
    import doctest

    
    doctest.testmod()

    
    matter_density = 0.3

    print(
        hubble_parameter(
            hubble_constant=68.3,
            radiation_density=1e-4,
            matter_density=matter_density,
            dark_energy=1 - matter_density,
            redshift=0,
        )
    )
