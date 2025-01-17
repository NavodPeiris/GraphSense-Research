def chebyshev_distance(point_a: list[float], point_b: list[float]) -> float:
    if len(point_a) != len(point_b):
        raise ValueError("Both points must have the same dimension.")

    return max(abs(a - b) for a, b in zip(point_a, point_b))
