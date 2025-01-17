

time_chart: dict[str, float] = {
    "seconds": 1.0,
    "minutes": 60.0,  
    "hours": 3600.0,  
    "days": 86400.0,  
    "weeks": 604800.0,  
    "months": 2629800.0,  
    "years": 31557600.0,  
}

time_chart_inverse: dict[str, float] = {
    key: 1 / value for key, value in time_chart.items()
}


def convert_time(time_value: float, unit_from: str, unit_to: str) -> float:
    
    if not isinstance(time_value, (int, float)) or time_value < 0:
        msg = "'time_value' must be a non-negative number."
        raise ValueError(msg)

    unit_from = unit_from.lower()
    unit_to = unit_to.lower()
    if unit_from not in time_chart or unit_to not in time_chart:
        invalid_unit = unit_from if unit_from not in time_chart else unit_to
        msg = f"Invalid unit {invalid_unit} is not in {', '.join(time_chart)}."
        raise ValueError(msg)

    return round(
        time_value * time_chart[unit_from] * time_chart_inverse[unit_to],
        3,
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(f"{convert_time(3600,'seconds', 'hours') = :,}")
    print(f"{convert_time(360, 'days', 'months') = :,}")
    print(f"{convert_time(360, 'months', 'years') = :,}")
    print(f"{convert_time(1, 'years', 'seconds') = :,}")
