
from typing import NamedTuple


class FromTo(NamedTuple):
    from_factor: float
    to_factor: float


TYPE_CONVERSION = {
    "millimeter": "mm",
    "centimeter": "cm",
    "meter": "m",
    "kilometer": "km",
    "inch": "in",
    "inche": "in",  
    "feet": "ft",
    "foot": "ft",
    "yard": "yd",
    "mile": "mi",
}

METRIC_CONVERSION = {
    "mm": FromTo(0.001, 1000),
    "cm": FromTo(0.01, 100),
    "m": FromTo(1, 1),
    "km": FromTo(1000, 0.001),
    "in": FromTo(0.0254, 39.3701),
    "ft": FromTo(0.3048, 3.28084),
    "yd": FromTo(0.9144, 1.09361),
    "mi": FromTo(1609.34, 0.000621371),
}


def length_conversion(value: float, from_type: str, to_type: str) -> float:
    
    new_from = from_type.lower().rstrip("s")
    new_from = TYPE_CONVERSION.get(new_from, new_from)
    new_to = to_type.lower().rstrip("s")
    new_to = TYPE_CONVERSION.get(new_to, new_to)
    if new_from not in METRIC_CONVERSION:
        msg = (
            f"Invalid 'from_type' value: {from_type!r}.\n"
            f"Conversion abbreviations are: {', '.join(METRIC_CONVERSION)}"
        )
        raise ValueError(msg)
    if new_to not in METRIC_CONVERSION:
        msg = (
            f"Invalid 'to_type' value: {to_type!r}.\n"
            f"Conversion abbreviations are: {', '.join(METRIC_CONVERSION)}"
        )
        raise ValueError(msg)
    return (
        value
        * METRIC_CONVERSION[new_from].from_factor
        * METRIC_CONVERSION[new_to].to_factor
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
