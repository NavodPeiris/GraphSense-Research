

from __future__ import annotations

from enum import Enum, unique
from typing import TypeVar

T = TypeVar("T", bound="Enum")


@unique
class BinaryUnit(Enum):
    yotta = 80
    zetta = 70
    exa = 60
    peta = 50
    tera = 40
    giga = 30
    mega = 20
    kilo = 10


@unique
class SIUnit(Enum):
    yotta = 24
    zetta = 21
    exa = 18
    peta = 15
    tera = 12
    giga = 9
    mega = 6
    kilo = 3
    hecto = 2
    deca = 1
    deci = -1
    centi = -2
    milli = -3
    micro = -6
    nano = -9
    pico = -12
    femto = -15
    atto = -18
    zepto = -21
    yocto = -24

    @classmethod
    def get_positive(cls: type[T]) -> dict:
        
        return {unit.name: unit.value for unit in cls if unit.value > 0}

    @classmethod
    def get_negative(cls: type[T]) -> dict:
        
        return {unit.name: unit.value for unit in cls if unit.value < 0}


def add_si_prefix(value: float) -> str:
    
    prefixes = SIUnit.get_positive() if value > 0 else SIUnit.get_negative()
    for name_prefix, value_prefix in prefixes.items():
        numerical_part = value / (10**value_prefix)
        if numerical_part > 1:
            return f"{numerical_part!s} {name_prefix}"
    return str(value)


def add_binary_prefix(value: float) -> str:
    
    for prefix in BinaryUnit:
        numerical_part = value / (2**prefix.value)
        if numerical_part > 1:
            return f"{numerical_part!s} {prefix.name}"
    return str(value)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
