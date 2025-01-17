

def rainfall_intensity(
    coefficient_k: float,
    coefficient_a: float,
    coefficient_b: float,
    coefficient_c: float,
    return_period: float,
    duration: float,
) -> float:
    if (
        coefficient_k <= 0
        or coefficient_a <= 0
        or coefficient_b <= 0
        or coefficient_c <= 0
        or return_period <= 0
        or duration <= 0
    ):
        raise ValueError("All parameters must be positive.")
    intensity = (coefficient_k * (return_period**coefficient_a)) / (
        (duration + coefficient_b) ** coefficient_c
    )
    return intensity


if __name__ == "__main__":
    import doctest

    doctest.testmod()
