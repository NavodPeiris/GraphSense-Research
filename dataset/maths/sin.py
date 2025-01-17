
from math import factorial, radians


def sin(
    angle_in_degrees: float, accuracy: int = 18, rounded_values_count: int = 10
) -> float:
    
    angle_in_degrees = angle_in_degrees - ((angle_in_degrees // 360.0) * 360.0)

    
    angle_in_radians = radians(angle_in_degrees)

    result = angle_in_radians
    a = 3
    b = -1

    for _ in range(accuracy):
        result += (b * (angle_in_radians**a)) / factorial(a)

        b = -b  
        a += 2  

    return round(result, rounded_values_count)


if __name__ == "__main__":
    __import__("doctest").testmod()
