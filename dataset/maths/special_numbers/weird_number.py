
from math import sqrt


def factors(number: int) -> list[int]:

    values = [1]
    for i in range(2, int(sqrt(number)) + 1, 1):
        if number % i == 0:
            values.append(i)
            if int(number // i) != i:
                values.append(int(number // i))
    return sorted(values)


def abundant(n: int) -> bool:
    return sum(factors(n)) > n


def semi_perfect(number: int) -> bool:
    values = factors(number)
    r = len(values)
    subset = [[0 for i in range(number + 1)] for j in range(r + 1)]
    for i in range(r + 1):
        subset[i][0] = True

    for i in range(1, number + 1):
        subset[0][i] = False

    for i in range(1, r + 1):
        for j in range(1, number + 1):
            if j < values[i - 1]:
                subset[i][j] = subset[i - 1][j]
            else:
                subset[i][j] = subset[i - 1][j] or subset[i - 1][j - values[i - 1]]

    return subset[r][number] != 0


def weird(number: int) -> bool:
    return abundant(number) and not semi_perfect(number)


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
    for number in (69, 70, 71):
        print(f"{number} is {'' if weird(number) else 'not '}weird.")
