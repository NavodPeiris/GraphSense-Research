

def partition(m: int) -> int:
    memo: list[list[int]] = [[0 for _ in range(m)] for _ in range(m + 1)]
    for i in range(m + 1):
        memo[i][0] = 1

    for n in range(m + 1):
        for k in range(1, m):
            memo[n][k] += memo[n][k - 1]
            if n - k > 0:
                memo[n][k] += memo[n - k - 1][k]

    return memo[m][m - 1]


if __name__ == "__main__":
    import sys

    if len(sys.argv) == 1:
        try:
            n = int(input("Enter a number: ").strip())
            print(partition(n))
        except ValueError:
            print("Please enter a number.")
    else:
        try:
            n = int(sys.argv[1])
            print(partition(n))
        except ValueError:
            print("Please pass a number.")
