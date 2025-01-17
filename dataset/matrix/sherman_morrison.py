from __future__ import annotations

from typing import Any


class Matrix:

    def __init__(self, row: int, column: int, default_value: float = 0) -> None:

        self.row, self.column = row, column
        self.array = [[default_value for _ in range(column)] for _ in range(row)]

    def __str__(self) -> str:

        
        s = f"Matrix consist of {self.row} rows and {self.column} columns\n"

        
        max_element_length = 0
        for row_vector in self.array:
            for obj in row_vector:
                max_element_length = max(max_element_length, len(str(obj)))
        string_format_identifier = f"%{max_element_length}s"

        
        def single_line(row_vector: list[float]) -> str:
            nonlocal string_format_identifier
            line = "["
            line += ", ".join(string_format_identifier % (obj,) for obj in row_vector)
            line += "]"
            return line

        s += "\n".join(single_line(row_vector) for row_vector in self.array)
        return s

    def __repr__(self) -> str:
        return str(self)

    def validate_indices(self, loc: tuple[int, int]) -> bool:
        if not (isinstance(loc, (list, tuple)) and len(loc) == 2):  
            return False
        elif not (0 <= loc[0] < self.row and 0 <= loc[1] < self.column):
            return False
        else:
            return True

    def __getitem__(self, loc: tuple[int, int]) -> Any:
        assert self.validate_indices(loc)
        return self.array[loc[0]][loc[1]]

    def __setitem__(self, loc: tuple[int, int], value: float) -> None:
        assert self.validate_indices(loc)
        self.array[loc[0]][loc[1]] = value

    def __add__(self, another: Matrix) -> Matrix:

        
        assert isinstance(another, Matrix)
        assert self.row == another.row
        assert self.column == another.column

        
        result = Matrix(self.row, self.column)
        for r in range(self.row):
            for c in range(self.column):
                result[r, c] = self[r, c] + another[r, c]
        return result

    def __neg__(self) -> Matrix:

        result = Matrix(self.row, self.column)
        for r in range(self.row):
            for c in range(self.column):
                result[r, c] = -self[r, c]
        return result

    def __sub__(self, another: Matrix) -> Matrix:
        return self + (-another)

    def __mul__(self, another: float | Matrix) -> Matrix:

        if isinstance(another, (int, float)):  
            result = Matrix(self.row, self.column)
            for r in range(self.row):
                for c in range(self.column):
                    result[r, c] = self[r, c] * another
            return result
        elif isinstance(another, Matrix):  
            assert self.column == another.row
            result = Matrix(self.row, another.column)
            for r in range(self.row):
                for c in range(another.column):
                    for i in range(self.column):
                        result[r, c] += self[r, i] * another[i, c]
            return result
        else:
            msg = f"Unsupported type given for another ({type(another)})"
            raise TypeError(msg)

    def transpose(self) -> Matrix:

        result = Matrix(self.column, self.row)
        for r in range(self.row):
            for c in range(self.column):
                result[c, r] = self[r, c]
        return result

    def sherman_morrison(self, u: Matrix, v: Matrix) -> Any:

        
        assert isinstance(u, Matrix)
        assert isinstance(v, Matrix)
        assert self.row == self.column == u.row == v.row  
        assert u.column == v.column == 1  

        
        v_t = v.transpose()
        numerator_factor = (v_t * self * u)[0, 0] + 1
        if numerator_factor == 0:
            return None  
        return self - ((self * u) * (v_t * self) * (1.0 / numerator_factor))



if __name__ == "__main__":

    def test1() -> None:
        
        ainv = Matrix(3, 3, 0)
        for i in range(3):
            ainv[i, i] = 1
        print(f"a^(-1) is {ainv}")
        
        u = Matrix(3, 1, 0)
        u[0, 0], u[1, 0], u[2, 0] = 1, 2, -3
        v = Matrix(3, 1, 0)
        v[0, 0], v[1, 0], v[2, 0] = 4, -2, 5
        print(f"u is {u}")
        print(f"v is {v}")
        print(f"uv^T is {u * v.transpose()}")
        
        print(f"(a + uv^T)^(-1) is {ainv.sherman_morrison(u, v)}")

    def test2() -> None:
        import doctest

        doctest.testmod()

    test2()
