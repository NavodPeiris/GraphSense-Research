def subset_combinations(elements: list[int], n: int) -> list:
    r = len(elements)
    if n > r:
        return []

    dp: list[list[tuple]] = [[] for _ in range(r + 1)]

    dp[0].append(())

    for i in range(1, r + 1):
        for j in range(i, 0, -1):
            for prev_combination in dp[j - 1]:
                dp[j].append((*prev_combination, elements[i - 1]))

    try:
        return sorted(dp[n])
    except TypeError:
        return dp[n]


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    print(f"{subset_combinations(elements=[10, 20, 30, 40], n=2) = }")
