
from __future__ import annotations

import math



def ucal(u: float, p: int) -> float:
    temp = u
    for i in range(1, p):
        temp = temp * (u - i)
    return temp


def main() -> None:
    n = int(input("enter the numbers of values: "))
    y: list[list[float]] = []
    for _ in range(n):
        y.append([])
    for i in range(n):
        for j in range(n):
            y[i].append(j)
            y[i][j] = 0

    print("enter the values of parameters in a list: ")
    x = list(map(int, input().split()))

    print("enter the values of corresponding parameters: ")
    for i in range(n):
        y[i][0] = float(input())

    value = int(input("enter the value to interpolate: "))
    u = (value - x[0]) / (x[1] - x[0])

    

    for i in range(1, n):
        for j in range(n - i):
            y[j][i] = y[j + 1][i - 1] - y[j][i - 1]

    summ = y[0][0]
    for i in range(1, n):
        summ += (ucal(u, i) * y[0][i]) / math.factorial(i)

    print(f"the value at {value} is {summ}")


if __name__ == "__main__":
    main()
