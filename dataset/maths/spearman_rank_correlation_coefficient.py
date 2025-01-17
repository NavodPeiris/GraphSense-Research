from collections.abc import Sequence


def assign_ranks(data: Sequence[float]) -> list[int]:
    ranked_data = sorted((value, index) for index, value in enumerate(data))
    ranks = [0] * len(data)

    for position, (_, index) in enumerate(ranked_data):
        ranks[index] = position + 1

    return ranks


def calculate_spearman_rank_correlation(
    variable_1: Sequence[float], variable_2: Sequence[float]
) -> float:
    n = len(variable_1)
    rank_var1 = assign_ranks(variable_1)
    rank_var2 = assign_ranks(variable_2)

    
    d = [rx - ry for rx, ry in zip(rank_var1, rank_var2)]

    
    d_squared = sum(di**2 for di in d)

    
    rho = 1 - (6 * d_squared) / (n * (n**2 - 1))

    return rho


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    
    print(
        f"{calculate_spearman_rank_correlation([1, 2, 3, 4, 5], [2, 4, 6, 8, 10]) = }"
    )

    print(f"{calculate_spearman_rank_correlation([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]) = }")

    print(f"{calculate_spearman_rank_correlation([1, 2, 3, 4, 5], [5, 1, 2, 9, 5]) = }")
