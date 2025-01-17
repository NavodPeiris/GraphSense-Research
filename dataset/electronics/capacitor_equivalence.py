

from __future__ import annotations


def capacitor_parallel(capacitors: list[float]) -> float:
    sum_c = 0.0
    for index, capacitor in enumerate(capacitors):
        if capacitor < 0:
            msg = f"Capacitor at index {index} has a negative value!"
            raise ValueError(msg)
        sum_c += capacitor
    return sum_c


def capacitor_series(capacitors: list[float]) -> float:

    first_sum = 0.0
    for index, capacitor in enumerate(capacitors):
        if capacitor <= 0:
            msg = f"Capacitor at index {index} has a negative or zero value!"
            raise ValueError(msg)
        first_sum += 1 / capacitor
    return 1 / first_sum


if __name__ == "__main__":
    import doctest

    doctest.testmod()
