from math import asin, atan, cos, radians, sin, sqrt, tan

AXIS_A = 6378137.0
AXIS_B = 6356752.314245
RADIUS = 6378137


def haversine_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    
    
    
    
    flattening = (AXIS_A - AXIS_B) / AXIS_A
    phi_1 = atan((1 - flattening) * tan(radians(lat1)))
    phi_2 = atan((1 - flattening) * tan(radians(lat2)))
    lambda_1 = radians(lon1)
    lambda_2 = radians(lon2)
    
    sin_sq_phi = sin((phi_2 - phi_1) / 2)
    sin_sq_lambda = sin((lambda_2 - lambda_1) / 2)
    
    sin_sq_phi *= sin_sq_phi
    sin_sq_lambda *= sin_sq_lambda
    h_value = sqrt(sin_sq_phi + (cos(phi_1) * cos(phi_2) * sin_sq_lambda))
    return 2 * RADIUS * asin(h_value)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
