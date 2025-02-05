
from __future__ import annotations


def get_valid_pos(position: tuple[int, int], n: int) -> list[tuple[int, int]]:
   
    y, x = position
    positions = [
        (y + 1, x + 2),
        (y - 1, x + 2),
        (y + 1, x - 2),
        (y - 1, x - 2),
        (y + 2, x + 1),
        (y + 2, x - 1),
        (y - 2, x + 1),
        (y - 2, x - 1),
    ]
    permissible_positions = []

    for inner_position in positions:
        y_test, x_test = inner_position
        if 0 <= y_test < n and 0 <= x_test < n:
            permissible_positions.append(inner_position)

    return permissible_positions


def is_complete(board: list[list[int]]) -> bool:
    
    return not any(elem == 0 for row in board for elem in row)


def open_knight_tour_helper(
    board: list[list[int]], pos: tuple[int, int], curr: int
) -> bool:
   
    if is_complete(board):
        return True

    for position in get_valid_pos(pos, len(board)):
        y, x = position

        if board[y][x] == 0:
            board[y][x] = curr + 1
            if open_knight_tour_helper(board, position, curr + 1):
                return True
            board[y][x] = 0

    return False


def open_knight_tour(n: int) -> list[list[int]]:
   

    board = [[0 for i in range(n)] for j in range(n)]

    for i in range(n):
        for j in range(n):
            board[i][j] = 1
            if open_knight_tour_helper(board, (i, j), 1):
                return board
            board[i][j] = 0

    msg = f"Open Knight Tour cannot be performed on a board of size {n}"
    raise ValueError(msg)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
