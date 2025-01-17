
from scipy.constants import g


def terminal_velocity(
    mass: float, density: float, area: float, drag_coefficient: float
) -> float:
    if mass <= 0 or density <= 0 or area <= 0 or drag_coefficient <= 0:
        raise ValueError(
            "mass, density, area and the drag coefficient all need to be positive"
        )
    return ((2 * mass * g) / (density * area * drag_coefficient)) ** 0.5


if __name__ == "__main__":
    import doctest

    doctest.testmod()
