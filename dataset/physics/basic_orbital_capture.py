
from math import pow, sqrt  

from scipy.constants import G, c, pi


def capture_radii(
    target_body_radius: float, target_body_mass: float, projectile_velocity: float
) -> float:

    if target_body_mass < 0:
        raise ValueError("Mass cannot be less than 0")
    if target_body_radius < 0:
        raise ValueError("Radius cannot be less than 0")
    if projectile_velocity > c:
        raise ValueError("Cannot go beyond speed of light")

    escape_velocity_squared = (2 * G * target_body_mass) / target_body_radius
    capture_radius = target_body_radius * sqrt(
        1 + escape_velocity_squared / pow(projectile_velocity, 2)
    )
    return round(capture_radius, 0)


def capture_area(capture_radius: float) -> float:

    if capture_radius < 0:
        raise ValueError("Cannot have a capture radius less than 0")
    sigma = pi * pow(capture_radius, 2)
    return round(sigma, 0)


if __name__ == "__main__":
    from doctest import testmod

    testmod()
