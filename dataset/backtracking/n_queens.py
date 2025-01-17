

from __future__ import annotations

solution = []


def is_safe(board: list[list[int]], row: int, column: int) -> bool:
    

    n = len(board)  

    
    return (
        all(board[i][j] != 1 for i, j in zip(range(row, -1, -1), range(column, n)))
        and all(
            board[i][j] != 1 for i, j in zip(range(row, -1, -1), range(column, -1, -1))
        )
        and all(board[i][j] != 1 for i, j in zip(range(row, n), range(column, n)))
        and all(board[i][j] != 1 for i, j in zip(range(row, n), range(column, -1, -1)))
    )


def solve(board: list[list[int]], row: int) -> bool:
    
    if row >= len(board):
        
        solution.append(board)
        printboard(board)
        print()
        return True
    for i in range(len(board)):
        
        if is_safe(board, row, i):
            board[row][i] = 1
            solve(board, row + 1)
            board[row][i] = 0
    return False


def printboard(board: list[list[int]]) -> None:
    
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                print("Q", end=" ")  
            else:
                print(".", end=" ")  
        print()


n = 8
board = [[0 for i in range(n)] for j in range(n)]
solve(board, 0)
print("The total number of solutions are:", len(solution))
