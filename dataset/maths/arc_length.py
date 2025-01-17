from math import pi


def arc_length(angle: int, radius: int) -> float:
    return 2 * pi * radius * (angle / 360)


if __name__ == "__main__":
    print(arc_length(90, 10))
