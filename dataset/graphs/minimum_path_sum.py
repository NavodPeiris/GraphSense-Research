def min_path_sum(grid: list) -> int:

    if not grid or not grid[0]:
        raise TypeError("The grid does not contain the appropriate information")

    for cell_n in range(1, len(grid[0])):
        grid[0][cell_n] += grid[0][cell_n - 1]
    row_above = grid[0]

    for row_n in range(1, len(grid)):
        current_row = grid[row_n]
        grid[row_n] = fill_row(current_row, row_above)
        row_above = grid[row_n]

    return grid[-1][-1]


def fill_row(current_row: list, row_above: list) -> list:

    current_row[0] += row_above[0]
    for cell_n in range(1, len(current_row)):
        current_row[cell_n] += min(current_row[cell_n - 1], row_above[cell_n])

    return current_row


if __name__ == "__main__":
    import doctest

    doctest.testmod()
