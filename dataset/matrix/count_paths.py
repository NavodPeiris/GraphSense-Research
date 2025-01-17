

def depth_first_search(grid: list[list[int]], row: int, col: int, visit: set) -> int:
    row_length, col_length = len(grid), len(grid[0])
    if (
        min(row, col) < 0
        or row == row_length
        or col == col_length
        or (row, col) in visit
        or grid[row][col] == 1
    ):
        return 0
    if row == row_length - 1 and col == col_length - 1:
        return 1

    visit.add((row, col))

    count = 0
    count += depth_first_search(grid, row + 1, col, visit)
    count += depth_first_search(grid, row - 1, col, visit)
    count += depth_first_search(grid, row, col + 1, visit)
    count += depth_first_search(grid, row, col - 1, visit)

    visit.remove((row, col))
    return count


if __name__ == "__main__":
    import doctest

    doctest.testmod()
