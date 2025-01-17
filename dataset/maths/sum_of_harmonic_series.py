def sum_of_harmonic_progression(
    first_term: float, common_difference: float, number_of_terms: int
) -> float:
    arithmetic_progression = [1 / first_term]
    first_term = 1 / first_term
    for _ in range(number_of_terms - 1):
        first_term += common_difference
        arithmetic_progression.append(first_term)
    harmonic_series = [1 / step for step in arithmetic_progression]
    return sum(harmonic_series)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(sum_of_harmonic_progression(1 / 2, 2, 2))
