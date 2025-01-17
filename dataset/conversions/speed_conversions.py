
speed_chart: dict[str, float] = {
    "km/h": 1.0,
    "m/s": 3.6,
    "mph": 1.609344,
    "knot": 1.852,
}

speed_chart_inverse: dict[str, float] = {
    "km/h": 1.0,
    "m/s": 0.277777778,
    "mph": 0.621371192,
    "knot": 0.539956803,
}


def convert_speed(speed: float, unit_from: str, unit_to: str) -> float:
    
    if unit_to not in speed_chart or unit_from not in speed_chart_inverse:
        msg = (
            f"Incorrect 'from_type' or 'to_type' value: {unit_from!r}, {unit_to!r}\n"
            f"Valid values are: {', '.join(speed_chart_inverse)}"
        )
        raise ValueError(msg)
    return round(speed * speed_chart[unit_from] * speed_chart_inverse[unit_to], 3)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
