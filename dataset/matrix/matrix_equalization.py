from sys import maxsize


def array_equalization(vector: list[int], step_size: int) -> int:
    if step_size <= 0:
        raise ValueError("Step size must be positive and non-zero.")
    if not isinstance(step_size, int):
        raise ValueError("Step size must be an integer.")

    unique_elements = set(vector)
    min_updates = maxsize

    for element in unique_elements:
        elem_index = 0
        updates = 0
        while elem_index < len(vector):
            if vector[elem_index] != element:
                updates += 1
                elem_index += step_size
            else:
                elem_index += 1
        min_updates = min(min_updates, updates)

    return min_updates


if __name__ == "__main__":
    from doctest import testmod

    testmod()
