

def rank_of_matrix(matrix: list[list[int | float]]) -> int:

    rows = len(matrix)
    columns = len(matrix[0])
    rank = min(rows, columns)

    for row in range(rank):
        
        if matrix[row][row] != 0:
            
            for col in range(row + 1, rows):
                multiplier = matrix[col][row] / matrix[row][row]
                for i in range(row, columns):
                    matrix[col][i] -= multiplier * matrix[row][i]
        else:
            
            reduce = True
            for i in range(row + 1, rows):
                if matrix[i][row] != 0:
                    matrix[row], matrix[i] = matrix[i], matrix[row]
                    reduce = False
                    break
            if reduce:
                rank -= 1
                for i in range(rows):
                    matrix[i][row] = matrix[i][rank]

            
            row -= 1

    return rank


if __name__ == "__main__":
    import doctest

    doctest.testmod()
