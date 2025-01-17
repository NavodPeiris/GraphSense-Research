

def multiply(matrix_a: list[list[int]], matrix_b: list[list[int]]) -> list[list[int]]:
    matrix_c = []
    n = len(matrix_a)
    for i in range(n):
        list_1 = []
        for j in range(n):
            val = 0
            for k in range(n):
                val = val + matrix_a[i][k] * matrix_b[k][j]
            list_1.append(val)
        matrix_c.append(list_1)
    return matrix_c


def identity(n: int) -> list[list[int]]:
    return [[int(row == column) for column in range(n)] for row in range(n)]


def nth_fibonacci_matrix(n: int) -> int:
    if n <= 1:
        return n
    res_matrix = identity(2)
    fibonacci_matrix = [[1, 1], [1, 0]]
    n = n - 1
    while n > 0:
        if n % 2 == 1:
            res_matrix = multiply(res_matrix, fibonacci_matrix)
        fibonacci_matrix = multiply(fibonacci_matrix, fibonacci_matrix)
        n = int(n / 2)
    return res_matrix[0][0]


def nth_fibonacci_bruteforce(n: int) -> int:
    if n <= 1:
        return n
    fib0 = 0
    fib1 = 1
    for _ in range(2, n + 1):
        fib0, fib1 = fib1, fib0 + fib1
    return fib1


def main() -> None:
    for ordinal in "0th 1st 2nd 3rd 10th 100th 1000th".split():
        n = int("".join(c for c in ordinal if c in "0123456789"))  
        print(
            f"{ordinal} fibonacci number using matrix exponentiation is "
            f"{nth_fibonacci_matrix(n)} and using bruteforce is "
            f"{nth_fibonacci_bruteforce(n)}\n"
        )
    
    
    
    
    
    
    


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
