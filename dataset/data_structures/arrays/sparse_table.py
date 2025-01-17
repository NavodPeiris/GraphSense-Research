

from math import log2


def build_sparse_table(number_list: list[int]) -> list[list[int]]:
    
    if not number_list:
        raise ValueError("empty number list not allowed")

    length = len(number_list)
    
    row = int(log2(length)) + 1
    sparse_table = [[0 for i in range(length)] for j in range(row)]

    
    for i, value in enumerate(number_list):
        sparse_table[0][i] = value
    j = 1

   
    while (1 << j) <= length:
        i = 0
        
        while (i + (1 << j) - 1) < length:
            
            sparse_table[j][i] = min(
                sparse_table[j - 1][i + (1 << (j - 1))], sparse_table[j - 1][i]
            )
            i += 1
        j += 1
    return sparse_table


def query(sparse_table: list[list[int]], left_bound: int, right_bound: int) -> int:
    
    if left_bound < 0 or right_bound >= len(sparse_table[0]):
        raise IndexError("list index out of range")

    
    j = int(log2(right_bound - left_bound + 1))

    
    return min(sparse_table[j][right_bound - (1 << j) + 1], sparse_table[j][left_bound])


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    print(f"{query(build_sparse_table([3, 1, 9]), 2, 2) = }")
