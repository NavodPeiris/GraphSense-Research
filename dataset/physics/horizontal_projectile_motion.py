


from math import radians as angle_to_radians
from math import sin


g = 9.80665


def check_args(init_velocity: float, angle: float) -> None:
    

    
    if not isinstance(init_velocity, (int, float)):
        raise TypeError("Invalid velocity. Should be a positive number.")

    if not isinstance(angle, (int, float)):
        raise TypeError("Invalid angle. Range is 1-90 degrees.")

    
    if angle > 90 or angle < 1:
        raise ValueError("Invalid angle. Range is 1-90 degrees.")

    
    if init_velocity < 0:
        raise ValueError("Invalid velocity. Should be a positive number.")


def horizontal_distance(init_velocity: float, angle: float) -> float:
    
    check_args(init_velocity, angle)
    radians = angle_to_radians(2 * angle)
    return round(init_velocity**2 * sin(radians) / g, 2)


def max_height(init_velocity: float, angle: float) -> float:
    
    check_args(init_velocity, angle)
    radians = angle_to_radians(angle)
    return round(init_velocity**2 * sin(radians) ** 2 / (2 * g), 2)


def total_time(init_velocity: float, angle: float) -> float:
    
    check_args(init_velocity, angle)
    radians = angle_to_radians(angle)
    return round(2 * init_velocity * sin(radians) / g, 2)


def test_motion() -> None:
    
    v0, angle = 25, 20
    assert horizontal_distance(v0, angle) == 40.97
    assert max_height(v0, angle) == 3.73
    assert total_time(v0, angle) == 1.74


if __name__ == "__main__":
    from doctest import testmod

    testmod()

    
    init_vel = float(input("Initial Velocity: ").strip())

    
    angle = float(input("angle: ").strip())

    
    print()
    print("Results: ")
    print(f"Horizontal Distance: {horizontal_distance(init_vel, angle)!s} [m]")
    print(f"Maximum Height: {max_height(init_vel, angle)!s} [m]")
    print(f"Total Time: {total_time(init_vel, angle)!s} [s]")
