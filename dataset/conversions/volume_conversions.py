
from typing import NamedTuple


class FromTo(NamedTuple):
    from_factor: float
    to_factor: float


METRIC_CONVERSION = {
    "cubic meter": FromTo(1, 1),
    "litre": FromTo(0.001, 1000),
    "kilolitre": FromTo(1, 1),
    "gallon": FromTo(0.00454, 264.172),
    "cubic yard": FromTo(0.76455, 1.30795),
    "cubic foot": FromTo(0.028, 35.3147),
    "cup": FromTo(0.000236588, 4226.75),
}


def volume_conversion(value: float, from_type: str, to_type: str) -> float:
    
    if from_type not in METRIC_CONVERSION:
        raise ValueError(
            f"Invalid 'from_type' value: {from_type!r}  Supported values are:\n"
            + ", ".join(METRIC_CONVERSION)
        )
    if to_type not in METRIC_CONVERSION:
        raise ValueError(
            f"Invalid 'to_type' value: {to_type!r}.  Supported values are:\n"
            + ", ".join(METRIC_CONVERSION)
        )
    return (
        value
        * METRIC_CONVERSION[from_type].from_factor
        * METRIC_CONVERSION[to_type].to_factor
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
