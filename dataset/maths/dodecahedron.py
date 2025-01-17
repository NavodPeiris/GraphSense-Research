



def dodecahedron_surface_area(edge: float) -> float:

    if edge <= 0 or not isinstance(edge, int):
        raise ValueError("Length must be a positive.")
    return 3 * ((25 + 10 * (5 ** (1 / 2))) ** (1 / 2)) * (edge**2)


def dodecahedron_volume(edge: float) -> float:

    if edge <= 0 or not isinstance(edge, int):
        raise ValueError("Length must be a positive.")
    return ((15 + (7 * (5 ** (1 / 2)))) / 4) * (edge**3)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
