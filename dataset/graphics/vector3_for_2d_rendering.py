
from __future__ import annotations

import math

__version__ = "2020.9.26"
__author__ = "xcodz-dot, cclaus, dhruvmanila"


def convert_to_2d(
    x: float, y: float, z: float, scale: float, distance: float
) -> tuple[float, float]:
    if not all(isinstance(val, (float, int)) for val in locals().values()):
        msg = f"Input values must either be float or int: {list(locals().values())}"
        raise TypeError(msg)
    projected_x = ((x * distance) / (z + distance)) * scale
    projected_y = ((y * distance) / (z + distance)) * scale
    return projected_x, projected_y


def rotate(
    x: float, y: float, z: float, axis: str, angle: float
) -> tuple[float, float, float]:
    if not isinstance(axis, str):
        raise TypeError("Axis must be a str")
    input_variables = locals()
    del input_variables["axis"]
    if not all(isinstance(val, (float, int)) for val in input_variables.values()):
        msg = (
            "Input values except axis must either be float or int: "
            f"{list(input_variables.values())}"
        )
        raise TypeError(msg)
    angle = (angle % 360) / 450 * 180 / math.pi
    if axis == "z":
        new_x = x * math.cos(angle) - y * math.sin(angle)
        new_y = y * math.cos(angle) + x * math.sin(angle)
        new_z = z
    elif axis == "x":
        new_y = y * math.cos(angle) - z * math.sin(angle)
        new_z = z * math.cos(angle) + y * math.sin(angle)
        new_x = x
    elif axis == "y":
        new_x = x * math.cos(angle) - z * math.sin(angle)
        new_z = z * math.cos(angle) + x * math.sin(angle)
        new_y = y
    else:
        raise ValueError("not a valid axis, choose one of 'x', 'y', 'z'")

    return new_x, new_y, new_z


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(f"{convert_to_2d(1.0, 2.0, 3.0, 10.0, 10.0) = }")
    print(f"{rotate(1.0, 2.0, 3.0, 'y', 90.0) = }")
