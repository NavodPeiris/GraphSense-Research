def minkowski_distance(
    point_a: list[float],
    point_b: list[float],
    order: int,
) -> float:
    if order < 1:
        raise ValueError("The order must be greater than or equal to 1.")

    if len(point_a) != len(point_b):
        raise ValueError("Both points must have the same dimension.")

    return sum(abs(a - b) ** order for a, b in zip(point_a, point_b)) ** (1 / order)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
