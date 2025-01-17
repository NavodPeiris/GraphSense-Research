

def focal_length_of_lens(
    object_distance_from_lens: float, image_distance_from_lens: float
) -> float:

    if object_distance_from_lens == 0 or image_distance_from_lens == 0:
        raise ValueError(
            "Invalid inputs. Enter non zero values with respect to the sign convention."
        )
    focal_length = 1 / (
        (1 / image_distance_from_lens) - (1 / object_distance_from_lens)
    )
    return focal_length


def object_distance(
    focal_length_of_lens: float, image_distance_from_lens: float
) -> float:

    if image_distance_from_lens == 0 or focal_length_of_lens == 0:
        raise ValueError(
            "Invalid inputs. Enter non zero values with respect to the sign convention."
        )

    object_distance = 1 / ((1 / image_distance_from_lens) - (1 / focal_length_of_lens))
    return object_distance


def image_distance(
    focal_length_of_lens: float, object_distance_from_lens: float
) -> float:
    if object_distance_from_lens == 0 or focal_length_of_lens == 0:
        raise ValueError(
            "Invalid inputs. Enter non zero values with respect to the sign convention."
        )
    image_distance = 1 / ((1 / object_distance_from_lens) + (1 / focal_length_of_lens))
    return image_distance
