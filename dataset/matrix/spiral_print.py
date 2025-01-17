

def check_matrix(matrix: list[list[int]]) -> bool:
    
    matrix = [list(row) for row in matrix]
    if matrix and isinstance(matrix, list):
        if isinstance(matrix[0], list):
            prev_len = 0
            for row in matrix:
                if prev_len == 0:
                    prev_len = len(row)
                    result = True
                else:
                    result = prev_len == len(row)
        else:
            result = True
    else:
        result = False

    return result


def spiral_print_clockwise(a: list[list[int]]) -> None:
    if check_matrix(a) and len(a) > 0:
        a = [list(row) for row in a]
        mat_row = len(a)
        if isinstance(a[0], list):
            mat_col = len(a[0])
        else:
            for dat in a:
                print(dat)
            return

        
        for i in range(mat_col):
            print(a[0][i])
        
        for i in range(1, mat_row):
            print(a[i][mat_col - 1])
        
        if mat_row > 1:
            for i in range(mat_col - 2, -1, -1):
                print(a[mat_row - 1][i])
        
        for i in range(mat_row - 2, 0, -1):
            print(a[i][0])
        remain_mat = [row[1 : mat_col - 1] for row in a[1 : mat_row - 1]]
        if len(remain_mat) > 0:
            spiral_print_clockwise(remain_mat)
        else:
            return
    else:
        print("Not a valid matrix")
        return





def spiral_traversal(matrix: list[list]) -> list[int]:
    if matrix:
        return list(matrix.pop(0)) + spiral_traversal(
            [list(row) for row in zip(*matrix)][::-1]
        )
    else:
        return []



if __name__ == "__main__":
    import doctest

    doctest.testmod()

    a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    spiral_print_clockwise(a)
