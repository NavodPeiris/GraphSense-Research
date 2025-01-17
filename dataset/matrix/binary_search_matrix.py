def binary_search(array: list, lower_bound: int, upper_bound: int, value: int) -> int:

    r = int((lower_bound + upper_bound) // 2)
    if array[r] == value:
        return r
    if lower_bound >= upper_bound:
        return -1
    if array[r] < value:
        return binary_search(array, r + 1, upper_bound, value)
    else:
        return binary_search(array, lower_bound, r - 1, value)


def mat_bin_search(value: int, matrix: list) -> list:
    index = 0
    if matrix[index][0] == value:
        return [index, 0]
    while index < len(matrix) and matrix[index][0] < value:
        r = binary_search(matrix[index], 0, len(matrix[index]) - 1, value)
        if r != -1:
            return [index, r]
        index += 1
    return [-1, -1]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
