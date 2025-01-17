

def neville_interpolate(x_points: list, y_points: list, x0: int) -> list:
    n = len(x_points)
    q = [[0] * n for i in range(n)]
    for i in range(n):
        q[i][1] = y_points[i]

    for i in range(2, n):
        for j in range(i, n):
            q[j][i] = (
                (x0 - x_points[j - i + 1]) * q[j][i - 1]
                - (x0 - x_points[j]) * q[j - 1][i - 1]
            ) / (x_points[j] - x_points[j - i + 1])

    return [q[n - 1][n - 1], q]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
