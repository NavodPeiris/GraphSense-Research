
UNIT_SYMBOL = {
    "meter": "m",
    "kilometer": "km",
    "megametre": "Mm",
    "gigametre": "Gm",
    "terametre": "Tm",
    "petametre": "Pm",
    "exametre": "Em",
    "zettametre": "Zm",
    "yottametre": "Ym",
}

METRIC_CONVERSION = {
    "m": 0,
    "km": 3,
    "Mm": 6,
    "Gm": 9,
    "Tm": 12,
    "Pm": 15,
    "Em": 18,
    "Zm": 21,
    "Ym": 24,
}


def length_conversion(value: float, from_type: str, to_type: str) -> float:
    
    from_sanitized = from_type.lower().strip("s")
    to_sanitized = to_type.lower().strip("s")

    from_sanitized = UNIT_SYMBOL.get(from_sanitized, from_sanitized)
    to_sanitized = UNIT_SYMBOL.get(to_sanitized, to_sanitized)

    if from_sanitized not in METRIC_CONVERSION:
        msg = (
            f"Invalid 'from_type' value: {from_type!r}.\n"
            f"Conversion abbreviations are: {', '.join(METRIC_CONVERSION)}"
        )
        raise ValueError(msg)
    if to_sanitized not in METRIC_CONVERSION:
        msg = (
            f"Invalid 'to_type' value: {to_type!r}.\n"
            f"Conversion abbreviations are: {', '.join(METRIC_CONVERSION)}"
        )
        raise ValueError(msg)
    from_exponent = METRIC_CONVERSION[from_sanitized]
    to_exponent = METRIC_CONVERSION[to_sanitized]
    exponent = 1

    if from_exponent > to_exponent:
        exponent = from_exponent - to_exponent
    else:
        exponent = -(to_exponent - from_exponent)

    return value * pow(10, exponent)


if __name__ == "__main__":
    from doctest import testmod

    testmod()
