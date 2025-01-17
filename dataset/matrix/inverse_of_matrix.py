from __future__ import annotations

from decimal import Decimal

from numpy import array


def inverse_of_matrix(matrix: list[list[float]]) -> list[list[float]]:

    d = Decimal

    
    
    if len(matrix) == 2 and len(matrix[0]) == 2 and len(matrix[1]) == 2:
        
        determinant = float(
            d(matrix[0][0]) * d(matrix[1][1]) - d(matrix[1][0]) * d(matrix[0][1])
        )
        if determinant == 0:
            raise ValueError("This matrix has no inverse.")

        
        swapped_matrix = [[0.0, 0.0], [0.0, 0.0]]
        swapped_matrix[0][0], swapped_matrix[1][1] = matrix[1][1], matrix[0][0]
        swapped_matrix[1][0], swapped_matrix[0][1] = -matrix[1][0], -matrix[0][1]

        
        return [
            [(float(d(n)) / determinant) or 0.0 for n in row] for row in swapped_matrix
        ]
    elif (
        len(matrix) == 3
        and len(matrix[0]) == 3
        and len(matrix[1]) == 3
        and len(matrix[2]) == 3
    ):
        
        determinant = float(
            (
                (d(matrix[0][0]) * d(matrix[1][1]) * d(matrix[2][2]))
                + (d(matrix[0][1]) * d(matrix[1][2]) * d(matrix[2][0]))
                + (d(matrix[0][2]) * d(matrix[1][0]) * d(matrix[2][1]))
            )
            - (
                (d(matrix[0][2]) * d(matrix[1][1]) * d(matrix[2][0]))
                + (d(matrix[0][1]) * d(matrix[1][0]) * d(matrix[2][2]))
                + (d(matrix[0][0]) * d(matrix[1][2]) * d(matrix[2][1]))
            )
        )
        if determinant == 0:
            raise ValueError("This matrix has no inverse.")

        
        cofactor_matrix = [
            [d(0.0), d(0.0), d(0.0)],
            [d(0.0), d(0.0), d(0.0)],
            [d(0.0), d(0.0), d(0.0)],
        ]
        cofactor_matrix[0][0] = (d(matrix[1][1]) * d(matrix[2][2])) - (
            d(matrix[1][2]) * d(matrix[2][1])
        )
        cofactor_matrix[0][1] = -(
            (d(matrix[1][0]) * d(matrix[2][2])) - (d(matrix[1][2]) * d(matrix[2][0]))
        )
        cofactor_matrix[0][2] = (d(matrix[1][0]) * d(matrix[2][1])) - (
            d(matrix[1][1]) * d(matrix[2][0])
        )
        cofactor_matrix[1][0] = -(
            (d(matrix[0][1]) * d(matrix[2][2])) - (d(matrix[0][2]) * d(matrix[2][1]))
        )
        cofactor_matrix[1][1] = (d(matrix[0][0]) * d(matrix[2][2])) - (
            d(matrix[0][2]) * d(matrix[2][0])
        )
        cofactor_matrix[1][2] = -(
            (d(matrix[0][0]) * d(matrix[2][1])) - (d(matrix[0][1]) * d(matrix[2][0]))
        )
        cofactor_matrix[2][0] = (d(matrix[0][1]) * d(matrix[1][2])) - (
            d(matrix[0][2]) * d(matrix[1][1])
        )
        cofactor_matrix[2][1] = -(
            (d(matrix[0][0]) * d(matrix[1][2])) - (d(matrix[0][2]) * d(matrix[1][0]))
        )
        cofactor_matrix[2][2] = (d(matrix[0][0]) * d(matrix[1][1])) - (
            d(matrix[0][1]) * d(matrix[1][0])
        )

        
        adjoint_matrix = array(cofactor_matrix)
        for i in range(3):
            for j in range(3):
                adjoint_matrix[i][j] = cofactor_matrix[j][i]

        
        inverse_matrix = array(cofactor_matrix)
        for i in range(3):
            for j in range(3):
                inverse_matrix[i][j] /= d(determinant)

        
        return [[float(d(n)) or 0.0 for n in row] for row in inverse_matrix]
    raise ValueError("Please provide a matrix of size 2x2 or 3x3.")
