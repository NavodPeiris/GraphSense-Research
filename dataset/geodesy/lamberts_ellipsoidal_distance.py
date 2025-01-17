from math import atan, cos, radians, sin, tan

from .haversine_distance import haversine_distance

AXIS_A = 6378137.0
AXIS_B = 6356752.314245
EQUATORIAL_RADIUS = 6378137


def lamberts_ellipsoidal_distance(
    lat1: float, lon1: float, lat2: float, lon2: float
) -> float:

    
    
    
    
    flattening = (AXIS_A - AXIS_B) / AXIS_A
    
    
    b_lat1 = atan((1 - flattening) * tan(radians(lat1)))
    b_lat2 = atan((1 - flattening) * tan(radians(lat2)))

    
    
    sigma = haversine_distance(lat1, lon1, lat2, lon2) / EQUATORIAL_RADIUS

    
    p_value = (b_lat1 + b_lat2) / 2
    q_value = (b_lat2 - b_lat1) / 2

    
    
    x_numerator = (sin(p_value) ** 2) * (cos(q_value) ** 2)
    x_demonimator = cos(sigma / 2) ** 2
    x_value = (sigma - sin(sigma)) * (x_numerator / x_demonimator)

    
    
    y_numerator = (cos(p_value) ** 2) * (sin(q_value) ** 2)
    y_denominator = sin(sigma / 2) ** 2
    y_value = (sigma + sin(sigma)) * (y_numerator / y_denominator)

    return EQUATORIAL_RADIUS * (sigma - ((flattening / 2) * (x_value + y_value)))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
