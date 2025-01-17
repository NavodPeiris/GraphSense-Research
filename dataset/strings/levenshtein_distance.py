from collections.abc import Callable


def levenshtein_distance(first_word: str, second_word: str) -> int:
    
    if len(first_word) < len(second_word):
        return levenshtein_distance(second_word, first_word)

    if len(second_word) == 0:
        return len(first_word)

    previous_row = list(range(len(second_word) + 1))

    for i, c1 in enumerate(first_word):
        current_row = [i + 1]

        for j, c2 in enumerate(second_word):
            
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)

            
            current_row.append(min(insertions, deletions, substitutions))

        
        previous_row = current_row

    
    return previous_row[-1]


def levenshtein_distance_optimized(first_word: str, second_word: str) -> int:
    if len(first_word) < len(second_word):
        return levenshtein_distance_optimized(second_word, first_word)

    if len(second_word) == 0:
        return len(first_word)

    previous_row = list(range(len(second_word) + 1))

    for i, c1 in enumerate(first_word):
        current_row = [i + 1] + [0] * len(second_word)

        for j, c2 in enumerate(second_word):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row[j + 1] = min(insertions, deletions, substitutions)

        previous_row = current_row

    return previous_row[-1]


def benchmark_levenshtein_distance(func: Callable) -> None:
    from timeit import timeit

    stmt = f"{func.__name__}('sitting', 'kitten')"
    setup = f"from __main__ import {func.__name__}"
    number = 25_000
    result = timeit(stmt=stmt, setup=setup, number=number)
    print(f"{func.__name__:<30} finished {number:,} runs in {result:.5f} seconds")


if __name__ == "__main__":
    
    first_word = input("Enter the first word for Levenshtein distance:\n").strip()
    second_word = input("Enter the second word for Levenshtein distance:\n").strip()

    
    print(f"{levenshtein_distance(first_word, second_word) = }")
    print(f"{levenshtein_distance_optimized(first_word, second_word) = }")

    
    benchmark_levenshtein_distance(levenshtein_distance)
    benchmark_levenshtein_distance(levenshtein_distance_optimized)
