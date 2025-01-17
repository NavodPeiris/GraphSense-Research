

def focal_length(distance_of_object: float, distance_of_image: float) -> float:

    if distance_of_object == 0 or distance_of_image == 0:
        raise ValueError(
            "Invalid inputs. Enter non zero values with respect to the sign convention."
        )
    focal_length = 1 / ((1 / distance_of_object) + (1 / distance_of_image))
    return focal_length


def object_distance(focal_length: float, distance_of_image: float) -> float:

    if distance_of_image == 0 or focal_length == 0:
        raise ValueError(
            "Invalid inputs. Enter non zero values with respect to the sign convention."
        )
    object_distance = 1 / ((1 / focal_length) - (1 / distance_of_image))
    return object_distance


def image_distance(focal_length: float, distance_of_object: float) -> float:

    if distance_of_object == 0 or focal_length == 0:
        raise ValueError(
            "Invalid inputs. Enter non zero values with respect to the sign convention."
        )
    image_distance = 1 / ((1 / focal_length) - (1 / distance_of_object))
    return image_distance
