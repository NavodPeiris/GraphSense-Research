

def match_pattern(input_string: str, pattern: str) -> bool:

    len_string = len(input_string) + 1
    len_pattern = len(pattern) + 1

    
    
    
    
    dp = [[0 for i in range(len_pattern)] for j in range(len_string)]

    
    dp[0][0] = 1

    
    for i in range(1, len_string):
        dp[i][0] = 0

    
    
    for j in range(1, len_pattern):
        dp[0][j] = dp[0][j - 2] if pattern[j - 1] == "*" else 0

    
    for i in range(1, len_string):
        for j in range(1, len_pattern):
            if input_string[i - 1] == pattern[j - 1] or pattern[j - 1] == ".":
                dp[i][j] = dp[i - 1][j - 1]

            elif pattern[j - 1] == "*":
                if dp[i][j - 2] == 1:
                    dp[i][j] = 1
                elif pattern[j - 2] in (input_string[i - 1], "."):
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = 0
            else:
                dp[i][j] = 0

    return bool(dp[-1][-1])


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    
    
    

    input_string = "aab"
    pattern = "c*a*b"

    
    if match_pattern(input_string, pattern):
        print(f"{input_string} matches the given pattern {pattern}")
    else:
        print(f"{input_string} does not match with the given pattern {pattern}")
