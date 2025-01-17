

def bell_numbers(max_set_length: int) -> list[int]:
    if max_set_length < 0:
        raise ValueError("max_set_length must be non-negative")

    bell = [0] * (max_set_length + 1)
    bell[0] = 1

    for i in range(1, max_set_length + 1):
        for j in range(i):
            bell[i] += _binomial_coefficient(i - 1, j) * bell[j]

    return bell


def _binomial_coefficient(total_elements: int, elements_to_choose: int) -> int:
    if elements_to_choose in {0, total_elements}:
        return 1

    elements_to_choose = min(elements_to_choose, total_elements - elements_to_choose)

    coefficient = 1
    for i in range(elements_to_choose):
        coefficient *= total_elements - i
        coefficient //= i + 1

    return coefficient


if __name__ == "__main__":
    import doctest

    doctest.testmod()
