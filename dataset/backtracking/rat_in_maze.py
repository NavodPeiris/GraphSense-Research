from __future__ import annotations


def solve_maze(
    maze: list[list[int]],
    source_row: int,
    source_column: int,
    destination_row: int,
    destination_column: int,
) -> list[list[int]]:
    
    size = len(maze)
    
    if not (0 <= source_row <= size - 1 and 0 <= source_column <= size - 1) or (
        not (0 <= destination_row <= size - 1 and 0 <= destination_column <= size - 1)
    ):
        raise ValueError("Invalid source or destination coordinates")
    
    solutions = [[1 for _ in range(size)] for _ in range(size)]
    solved = run_maze(
        maze, source_row, source_column, destination_row, destination_column, solutions
    )
    if solved:
        return solutions
    else:
        raise ValueError("No solution exists!")


def run_maze(
    maze: list[list[int]],
    i: int,
    j: int,
    destination_row: int,
    destination_column: int,
    solutions: list[list[int]],
) -> bool:
   
    size = len(maze)
    
    if i == destination_row and j == destination_column and maze[i][j] == 0:
        solutions[i][j] = 0
        return True

    lower_flag = (not i < 0) and (not j < 0)
    upper_flag = (i < size) and (j < size)  

    if lower_flag and upper_flag:
        
        block_flag = (solutions[i][j]) and (not maze[i][j])
        if block_flag:
            
            solutions[i][j] = 0

           
            if (
                run_maze(maze, i + 1, j, destination_row, destination_column, solutions)
                or run_maze(
                    maze, i, j + 1, destination_row, destination_column, solutions
                )
                or run_maze(
                    maze, i - 1, j, destination_row, destination_column, solutions
                )
                or run_maze(
                    maze, i, j - 1, destination_row, destination_column, solutions
                )
            ):
                return True

            solutions[i][j] = 1
            return False
    return False


if __name__ == "__main__":
    import doctest

    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
