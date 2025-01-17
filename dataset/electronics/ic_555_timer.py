from __future__ import annotations



def astable_frequency(
    resistance_1: float, resistance_2: float, capacitance: float
) -> float:

    if resistance_1 <= 0 or resistance_2 <= 0 or capacitance <= 0:
        raise ValueError("All values must be positive")
    return (1.44 / ((resistance_1 + 2 * resistance_2) * capacitance)) * 10**6


def astable_duty_cycle(resistance_1: float, resistance_2: float) -> float:

    if resistance_1 <= 0 or resistance_2 <= 0:
        raise ValueError("All values must be positive")
    return (resistance_1 + resistance_2) / (resistance_1 + 2 * resistance_2) * 100


if __name__ == "__main__":
    import doctest

    doctest.testmod()
