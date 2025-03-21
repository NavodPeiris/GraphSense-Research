
from __future__ import annotations


def make_matrix(row_size: int = 4) -> list[list[int]]:
    row_size = abs(row_size) or 4
    return [[1 + x + y * row_size for x in range(row_size)] for y in range(row_size)]


def rotate_90(matrix: list[list[int]]) -> list[list[int]]:

    return reverse_row(transpose(matrix))
    


def rotate_180(matrix: list[list[int]]) -> list[list[int]]:

    return reverse_row(reverse_column(matrix))
    


def rotate_270(matrix: list[list[int]]) -> list[list[int]]:

    return reverse_column(transpose(matrix))
    


def transpose(matrix: list[list[int]]) -> list[list[int]]:
    matrix[:] = [list(x) for x in zip(*matrix)]
    return matrix


def reverse_row(matrix: list[list[int]]) -> list[list[int]]:
    matrix[:] = matrix[::-1]
    return matrix


def reverse_column(matrix: list[list[int]]) -> list[list[int]]:
    matrix[:] = [x[::-1] for x in matrix]
    return matrix


def print_matrix(matrix: list[list[int]]) -> None:
    for i in matrix:
        print(*i)


if __name__ == "__main__":
    matrix = make_matrix()
    print("\norigin:\n")
    print_matrix(matrix)
    print("\nrotate 90 counterclockwise:\n")
    print_matrix(rotate_90(matrix))

    matrix = make_matrix()
    print("\norigin:\n")
    print_matrix(matrix)
    print("\nrotate 180:\n")
    print_matrix(rotate_180(matrix))

    matrix = make_matrix()
    print("\norigin:\n")
    print_matrix(matrix)
    print("\nrotate 270 counterclockwise:\n")
    print_matrix(rotate_270(matrix))
