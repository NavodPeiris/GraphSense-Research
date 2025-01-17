

def damerau_levenshtein_distance(first_string: str, second_string: str) -> int:
    
    dp_matrix = [[0] * (len(second_string) + 1) for _ in range(len(first_string) + 1)]

    
    for i in range(len(first_string) + 1):
        dp_matrix[i][0] = i
    for j in range(len(second_string) + 1):
        dp_matrix[0][j] = j

    
    for i, first_char in enumerate(first_string, start=1):
        for j, second_char in enumerate(second_string, start=1):
            cost = int(first_char != second_char)

            dp_matrix[i][j] = min(
                dp_matrix[i - 1][j] + 1,  
                dp_matrix[i][j - 1] + 1,  
                dp_matrix[i - 1][j - 1] + cost,  
            )

            if (
                i > 1
                and j > 1
                and first_string[i - 1] == second_string[j - 2]
                and first_string[i - 2] == second_string[j - 1]
            ):
                
                dp_matrix[i][j] = min(dp_matrix[i][j], dp_matrix[i - 2][j - 2] + cost)

    return dp_matrix[-1][-1]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
