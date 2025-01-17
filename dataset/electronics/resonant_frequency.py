


from __future__ import annotations

from math import pi, sqrt


def resonant_frequency(inductance: float, capacitance: float) -> tuple:

    if inductance <= 0:
        raise ValueError("Inductance cannot be 0 or negative")

    elif capacitance <= 0:
        raise ValueError("Capacitance cannot be 0 or negative")

    else:
        return (
            "Resonant frequency",
            float(1 / (2 * pi * (sqrt(inductance * capacitance)))),
        )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
