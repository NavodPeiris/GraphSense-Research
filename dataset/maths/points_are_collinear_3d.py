
Vector3d = tuple[float, float, float]
Point3d = tuple[float, float, float]


def create_vector(end_point1: Point3d, end_point2: Point3d) -> Vector3d:
    x = end_point2[0] - end_point1[0]
    y = end_point2[1] - end_point1[1]
    z = end_point2[2] - end_point1[2]
    return (x, y, z)


def get_3d_vectors_cross(ab: Vector3d, ac: Vector3d) -> Vector3d:
    x = ab[1] * ac[2] - ab[2] * ac[1]  
    y = (ab[0] * ac[2] - ab[2] * ac[0]) * -1  
    z = ab[0] * ac[1] - ab[1] * ac[0]  
    return (x, y, z)


def is_zero_vector(vector: Vector3d, accuracy: int) -> bool:
    return tuple(round(x, accuracy) for x in vector) == (0, 0, 0)


def are_collinear(a: Point3d, b: Point3d, c: Point3d, accuracy: int = 10) -> bool:
    ab = create_vector(a, b)
    ac = create_vector(a, c)
    return is_zero_vector(get_3d_vectors_cross(ab, ac), accuracy)
