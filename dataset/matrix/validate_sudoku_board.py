
from collections import defaultdict

NUM_SQUARES = 9
EMPTY_CELL = "."


def is_valid_sudoku_board(sudoku_board: list[list[str]]) -> bool:
    if len(sudoku_board) != NUM_SQUARES or (
        any(len(row) != NUM_SQUARES for row in sudoku_board)
    ):
        error_message = f"Sudoku boards must be {NUM_SQUARES}x{NUM_SQUARES} squares."
        raise ValueError(error_message)

    row_values: defaultdict[int, set[str]] = defaultdict(set)
    col_values: defaultdict[int, set[str]] = defaultdict(set)
    box_values: defaultdict[tuple[int, int], set[str]] = defaultdict(set)

    for row in range(NUM_SQUARES):
        for col in range(NUM_SQUARES):
            value = sudoku_board[row][col]

            if value == EMPTY_CELL:
                continue

            box = (row // 3, col // 3)

            if (
                value in row_values[row]
                or value in col_values[col]
                or value in box_values[box]
            ):
                return False

            row_values[row].add(value)
            col_values[col].add(value)
            box_values[box].add(value)

    return True


if __name__ == "__main__":
    from doctest import testmod
    from timeit import timeit

    testmod()
    print(timeit("is_valid_sudoku_board(valid_board)", globals=globals()))
    print(timeit("is_valid_sudoku_board(invalid_board)", globals=globals()))
