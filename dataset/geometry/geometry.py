from __future__ import annotations

import math
from dataclasses import dataclass, field
from types import NoneType
from typing import Self




@dataclass
class Angle:

    degrees: float = 90

    def __post_init__(self) -> None:
        if not isinstance(self.degrees, (int, float)) or not 0 <= self.degrees <= 360:
            raise TypeError("degrees must be a numeric value between 0 and 360.")


@dataclass
class Side:

    length: float
    angle: Angle = field(default_factory=Angle)
    next_side: Side | None = None

    def __post_init__(self) -> None:
        if not isinstance(self.length, (int, float)) or self.length <= 0:
            raise TypeError("length must be a positive numeric value.")
        if not isinstance(self.angle, Angle):
            raise TypeError("angle must be an Angle object.")
        if not isinstance(self.next_side, (Side, NoneType)):
            raise TypeError("next_side must be a Side or None.")


@dataclass
class Ellipse:

    major_radius: float
    minor_radius: float

    @property
    def area(self) -> float:
        return math.pi * self.major_radius * self.minor_radius

    @property
    def perimeter(self) -> float:
        return math.pi * (self.major_radius + self.minor_radius)


class Circle(Ellipse):

    def __init__(self, radius: float) -> None:
        super().__init__(radius, radius)
        self.radius = radius

    def __repr__(self) -> str:
        return f"Circle(radius={self.radius})"

    @property
    def diameter(self) -> float:
        return self.radius * 2

    def max_parts(self, num_cuts: float) -> float:
        if not isinstance(num_cuts, (int, float)) or num_cuts < 0:
            raise TypeError("num_cuts must be a positive numeric value.")
        return (num_cuts + 2 + num_cuts**2) * 0.5


@dataclass
class Polygon:

    sides: list[Side] = field(default_factory=list)

    def add_side(self, side: Side) -> Self:
        self.sides.append(side)
        return self

    def get_side(self, index: int) -> Side:
        return self.sides[index]

    def set_side(self, index: int, side: Side) -> Self:
        self.sides[index] = side
        return self


class Rectangle(Polygon):

    def __init__(self, short_side_length: float, long_side_length: float) -> None:
        super().__init__()
        self.short_side_length = short_side_length
        self.long_side_length = long_side_length
        self.post_init()

    def post_init(self) -> None:
        self.short_side = Side(self.short_side_length)
        self.long_side = Side(self.long_side_length)
        super().add_side(self.short_side)
        super().add_side(self.long_side)

    def perimeter(self) -> float:
        return (self.short_side.length + self.long_side.length) * 2

    def area(self) -> float:
        return self.short_side.length * self.long_side.length


@dataclass
class Square(Rectangle):

    def __init__(self, side_length: float) -> None:
        super().__init__(side_length, side_length)

    def perimeter(self) -> float:
        return super().perimeter()

    def area(self) -> float:
        return super().area()


if __name__ == "__main__":
    __import__("doctest").testmod()
