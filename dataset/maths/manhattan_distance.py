def manhattan_distance(point_a: list, point_b: list) -> float:

    _validate_point(point_a)
    _validate_point(point_b)
    if len(point_a) != len(point_b):
        raise ValueError("Both points must be in the same n-dimensional space")

    return float(sum(abs(a - b) for a, b in zip(point_a, point_b)))


def _validate_point(point: list[float]) -> None:
    if point:
        if isinstance(point, list):
            for item in point:
                if not isinstance(item, (int, float)):
                    msg = (
                        "Expected a list of numbers as input, found "
                        f"{type(item).__name__}"
                    )
                    raise TypeError(msg)
        else:
            msg = f"Expected a list of numbers as input, found {type(point).__name__}"
            raise TypeError(msg)
    else:
        raise ValueError("Missing an input")


def manhattan_distance_one_liner(point_a: list, point_b: list) -> float:

    _validate_point(point_a)
    _validate_point(point_b)
    if len(point_a) != len(point_b):
        raise ValueError("Both points must be in the same n-dimensional space")

    return float(sum(abs(x - y) for x, y in zip(point_a, point_b)))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
