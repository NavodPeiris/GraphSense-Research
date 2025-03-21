
import timeit



class Matrix:
    def __init__(self, arg):
        if isinstance(arg, list):  
            self.t = arg
            self.n = len(arg)
        else:  
            self.n = arg
            self.t = [[0 for _ in range(self.n)] for _ in range(self.n)]

    def __mul__(self, b):
        matrix = Matrix(self.n)
        for i in range(self.n):
            for j in range(self.n):
                for k in range(self.n):
                    matrix.t[i][j] += self.t[i][k] * b.t[k][j]
        return matrix


def modular_exponentiation(a, b):
    matrix = Matrix([[1, 0], [0, 1]])
    while b > 0:
        if b & 1:
            matrix *= a
        a *= a
        b >>= 1
    return matrix


def fibonacci_with_matrix_exponentiation(n, f1, f2):
    
    if n == 1:
        return f1
    elif n == 2:
        return f2
    matrix = Matrix([[1, 1], [1, 0]])
    matrix = modular_exponentiation(matrix, n - 2)
    return f2 * matrix.t[0][0] + f1 * matrix.t[0][1]


def simple_fibonacci(n, f1, f2):
    
    if n == 1:
        return f1
    elif n == 2:
        return f2

    n -= 2

    while n > 0:
        f2, f1 = f1 + f2, f2
        n -= 1

    return f2


def matrix_exponentiation_time():
    setup = """
from random import randint
from __main__ import fibonacci_with_matrix_exponentiation
    code = "simple_fibonacci(randint(1,70000), 1, 1)"
    exec_time = timeit.timeit(setup=setup, stmt=code, number=100)
    print(
        "Without matrix exponentiation the average execution time is ", exec_time / 100
    )
    return exec_time


def main():
    matrix_exponentiation_time()
    simple_fibonacci_time()


if __name__ == "__main__":
    main()
