

def validate_matrix_size(size: int) -> None:
    if not isinstance(size, int) or size <= 0:
        raise ValueError("Matrix size must be a positive integer.")


def validate_matrix_content(matrix: list[str], size: int) -> None:
    print(matrix)
    if len(matrix) != size:
        raise ValueError("The matrix dont match with size.")
    for row in matrix:
        if len(row) != size:
            msg = f"Each row in the matrix must have exactly {size} characters."
            raise ValueError(msg)
        if not all(char.isalnum() for char in row):
            raise ValueError("Matrix rows can only contain letters and numbers.")


def validate_moves(moves: list[tuple[int, int]], size: int) -> None:
    for move in moves:
        x, y = move
        if not (0 <= x < size and 0 <= y < size):
            raise ValueError("Move is out of bounds for a matrix.")


def parse_moves(input_str: str) -> list[tuple[int, int]]:
    moves = []
    for pair in input_str.split(","):
        parts = pair.strip().split()
        if len(parts) != 2:
            raise ValueError("Each move must have exactly two numbers.")
        x, y = map(int, parts)
        moves.append((x, y))
    return moves


def find_repeat(
    matrix_g: list[list[str]], row: int, column: int, size: int
) -> set[tuple[int, int]]:

    column = size - 1 - column
    visited = set()
    repeated = set()

    if (color := matrix_g[column][row]) != "-":

        def dfs(row_n: int, column_n: int) -> None:
            if row_n < 0 or row_n >= size or column_n < 0 or column_n >= size:
                return
            if (row_n, column_n) in visited:
                return
            visited.add((row_n, column_n))
            if matrix_g[row_n][column_n] == color:
                repeated.add((row_n, column_n))
                dfs(row_n - 1, column_n)
                dfs(row_n + 1, column_n)
                dfs(row_n, column_n - 1)
                dfs(row_n, column_n + 1)

        dfs(column, row)

    return repeated


def increment_score(count: int) -> int:
    return int(count * (count + 1) / 2)


def move_x(matrix_g: list[list[str]], column: int, size: int) -> list[list[str]]:

    new_list = []

    for row in range(size):
        if matrix_g[row][column] != "-":
            new_list.append(matrix_g[row][column])
        else:
            new_list.insert(0, matrix_g[row][column])
    for row in range(size):
        matrix_g[row][column] = new_list[row]
    return matrix_g


def move_y(matrix_g: list[list[str]], size: int) -> list[list[str]]:

    empty_columns = []

    for column in range(size - 1, -1, -1):
        if all(matrix_g[row][column] == "-" for row in range(size)):
            empty_columns.append(column)

    for column in empty_columns:
        for col in range(column + 1, size):
            for row in range(size):
                matrix_g[row][col - 1] = matrix_g[row][col]
        for row in range(size):
            matrix_g[row][-1] = "-"

    return matrix_g


def play(
    matrix_g: list[list[str]], pos_x: int, pos_y: int, size: int
) -> tuple[list[list[str]], int]:

    same_colors = find_repeat(matrix_g, pos_x, pos_y, size)

    if len(same_colors) != 0:
        for pos in same_colors:
            matrix_g[pos[0]][pos[1]] = "-"
        for column in range(size):
            matrix_g = move_x(matrix_g, column, size)

        matrix_g = move_y(matrix_g, size)

    return (matrix_g, increment_score(len(same_colors)))


def process_game(size: int, matrix: list[str], moves: list[tuple[int, int]]) -> int:

    game_matrix = [list(row) for row in matrix]
    total_score = 0

    for move in moves:
        pos_x, pos_y = move
        game_matrix, score = play(game_matrix, pos_x, pos_y, size)
        total_score += score

    return total_score


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
    try:
        size = int(input("Enter the size of the matrix: "))
        validate_matrix_size(size)
        print(f"Enter the {size} rows of the matrix:")
        matrix = [input(f"Row {i + 1}: ") for i in range(size)]
        validate_matrix_content(matrix, size)
        moves_input = input("Enter the moves (e.g., '0 0, 1 1'): ")
        moves = parse_moves(moves_input)
        validate_moves(moves, size)
        score = process_game(size, matrix, moves)
        print(f"Total score: {score}")
    except ValueError as e:
        print(f"{e}")
