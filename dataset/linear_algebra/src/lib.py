
from __future__ import annotations

import math
import random
from collections.abc import Collection
from typing import overload


class Vector:

    def __init__(self, components: Collection[float] | None = None) -> None:
        if components is None:
            components = []
        self.__components = list(components)

    def __len__(self) -> int:
        return len(self.__components)

    def __str__(self) -> str:
        return "(" + ",".join(map(str, self.__components)) + ")"

    def __add__(self, other: Vector) -> Vector:
        size = len(self)
        if size == len(other):
            result = [self.__components[i] + other.component(i) for i in range(size)]
            return Vector(result)
        else:
            raise Exception("must have the same size")

    def __sub__(self, other: Vector) -> Vector:
        size = len(self)
        if size == len(other):
            result = [self.__components[i] - other.component(i) for i in range(size)]
            return Vector(result)
        else:  
            raise Exception("must have the same size")

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vector):
            return NotImplemented
        if len(self) != len(other):
            return False
        return all(self.component(i) == other.component(i) for i in range(len(self)))

    @overload
    def __mul__(self, other: float) -> Vector: ...

    @overload
    def __mul__(self, other: Vector) -> float: ...

    def __mul__(self, other: float | Vector) -> float | Vector:
        if isinstance(other, (float, int)):
            ans = [c * other for c in self.__components]
            return Vector(ans)
        elif isinstance(other, Vector) and len(self) == len(other):
            size = len(self)
            prods = [self.__components[i] * other.component(i) for i in range(size)]
            return sum(prods)
        else:  
            raise Exception("invalid operand!")

    def copy(self) -> Vector:
        return Vector(self.__components)

    def component(self, i: int) -> float:
        if isinstance(i, int) and -len(self.__components) <= i < len(self.__components):
            return self.__components[i]
        else:
            raise Exception("index out of range")

    def change_component(self, pos: int, value: float) -> None:
        
        assert -len(self.__components) <= pos < len(self.__components)
        self.__components[pos] = value

    def euclidean_length(self) -> float:
        if len(self.__components) == 0:
            raise Exception("Vector is empty")
        squares = [c**2 for c in self.__components]
        return math.sqrt(sum(squares))

    def angle(self, other: Vector, deg: bool = False) -> float:
        num = self * other
        den = self.euclidean_length() * other.euclidean_length()
        if deg:
            return math.degrees(math.acos(num / den))
        else:
            return math.acos(num / den)


def zero_vector(dimension: int) -> Vector:
    
    assert isinstance(dimension, int)
    return Vector([0] * dimension)


def unit_basis_vector(dimension: int, pos: int) -> Vector:
    
    assert isinstance(dimension, int)
    assert isinstance(pos, int)
    ans = [0] * dimension
    ans[pos] = 1
    return Vector(ans)


def axpy(scalar: float, x: Vector, y: Vector) -> Vector:
    
    assert isinstance(x, Vector)
    assert isinstance(y, Vector)
    assert isinstance(scalar, (int, float))
    return x * scalar + y


def random_vector(n: int, a: int, b: int) -> Vector:
    random.seed(None)
    ans = [random.randint(a, b) for _ in range(n)]
    return Vector(ans)


class Matrix:

    def __init__(self, matrix: list[list[float]], w: int, h: int) -> None:
        self.__matrix = matrix
        self.__width = w
        self.__height = h

    def __str__(self) -> str:
        ans = ""
        for i in range(self.__height):
            ans += "|"
            for j in range(self.__width):
                if j < self.__width - 1:
                    ans += str(self.__matrix[i][j]) + ","
                else:
                    ans += str(self.__matrix[i][j]) + "|\n"
        return ans

    def __add__(self, other: Matrix) -> Matrix:
        if self.__width == other.width() and self.__height == other.height():
            matrix = []
            for i in range(self.__height):
                row = [
                    self.__matrix[i][j] + other.component(i, j)
                    for j in range(self.__width)
                ]
                matrix.append(row)
            return Matrix(matrix, self.__width, self.__height)
        else:
            raise Exception("matrix must have the same dimension!")

    def __sub__(self, other: Matrix) -> Matrix:
        if self.__width == other.width() and self.__height == other.height():
            matrix = []
            for i in range(self.__height):
                row = [
                    self.__matrix[i][j] - other.component(i, j)
                    for j in range(self.__width)
                ]
                matrix.append(row)
            return Matrix(matrix, self.__width, self.__height)
        else:
            raise Exception("matrices must have the same dimension!")

    @overload
    def __mul__(self, other: float) -> Matrix: ...

    @overload
    def __mul__(self, other: Vector) -> Vector: ...

    def __mul__(self, other: float | Vector) -> Vector | Matrix:
        if isinstance(other, Vector):  
            if len(other) == self.__width:
                ans = zero_vector(self.__height)
                for i in range(self.__height):
                    prods = [
                        self.__matrix[i][j] * other.component(j)
                        for j in range(self.__width)
                    ]
                    ans.change_component(i, sum(prods))
                return ans
            else:
                raise Exception(
                    "vector must have the same size as the "
                    "number of columns of the matrix!"
                )
        elif isinstance(other, (int, float)):  
            matrix = [
                [self.__matrix[i][j] * other for j in range(self.__width)]
                for i in range(self.__height)
            ]
            return Matrix(matrix, self.__width, self.__height)
        return None

    def height(self) -> int:
        return self.__height

    def width(self) -> int:
        return self.__width

    def component(self, x: int, y: int) -> float:
        if 0 <= x < self.__height and 0 <= y < self.__width:
            return self.__matrix[x][y]
        else:
            raise Exception("change_component: indices out of bounds")

    def change_component(self, x: int, y: int, value: float) -> None:
        if 0 <= x < self.__height and 0 <= y < self.__width:
            self.__matrix[x][y] = value
        else:
            raise Exception("change_component: indices out of bounds")

    def minor(self, x: int, y: int) -> float:
        if self.__height != self.__width:
            raise Exception("Matrix is not square")
        minor = self.__matrix[:x] + self.__matrix[x + 1 :]
        for i in range(len(minor)):
            minor[i] = minor[i][:y] + minor[i][y + 1 :]
        return Matrix(minor, self.__width - 1, self.__height - 1).determinant()

    def cofactor(self, x: int, y: int) -> float:
        if self.__height != self.__width:
            raise Exception("Matrix is not square")
        if 0 <= x < self.__height and 0 <= y < self.__width:
            return (-1) ** (x + y) * self.minor(x, y)
        else:
            raise Exception("Indices out of bounds")

    def determinant(self) -> float:
        if self.__height != self.__width:
            raise Exception("Matrix is not square")
        if self.__height < 1:
            raise Exception("Matrix has no element")
        elif self.__height == 1:
            return self.__matrix[0][0]
        elif self.__height == 2:
            return (
                self.__matrix[0][0] * self.__matrix[1][1]
                - self.__matrix[0][1] * self.__matrix[1][0]
            )
        else:
            cofactor_prods = [
                self.__matrix[0][y] * self.cofactor(0, y) for y in range(self.__width)
            ]
            return sum(cofactor_prods)


def square_zero_matrix(n: int) -> Matrix:
    ans: list[list[float]] = [[0] * n for _ in range(n)]
    return Matrix(ans, n, n)


def random_matrix(width: int, height: int, a: int, b: int) -> Matrix:
    random.seed(None)
    matrix: list[list[float]] = [
        [random.randint(a, b) for _ in range(width)] for _ in range(height)
    ]
    return Matrix(matrix, width, height)
