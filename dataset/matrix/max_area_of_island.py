
matrix = [
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
]


def is_safe(row: int, col: int, rows: int, cols: int) -> bool:
    return 0 <= row < rows and 0 <= col < cols


def depth_first_search(row: int, col: int, seen: set, mat: list[list[int]]) -> int:
    rows = len(mat)
    cols = len(mat[0])
    if is_safe(row, col, rows, cols) and (row, col) not in seen and mat[row][col] == 1:
        seen.add((row, col))
        return (
            1
            + depth_first_search(row + 1, col, seen, mat)
            + depth_first_search(row - 1, col, seen, mat)
            + depth_first_search(row, col + 1, seen, mat)
            + depth_first_search(row, col - 1, seen, mat)
        )
    else:
        return 0


def find_max_area(mat: list[list[int]]) -> int:
    seen: set = set()

    max_area = 0
    for row, line in enumerate(mat):
        for col, item in enumerate(line):
            if item == 1 and (row, col) not in seen:
                
                max_area = max(max_area, depth_first_search(row, col, seen, mat))
    return max_area


if __name__ == "__main__":
    import doctest

    print(find_max_area(matrix))  


    doctest.testmod()
