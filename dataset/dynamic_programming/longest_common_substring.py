

def longest_common_substring(text1: str, text2: str) -> str:

    if not (isinstance(text1, str) and isinstance(text2, str)):
        raise ValueError("longest_common_substring() takes two strings for inputs")

    text1_length = len(text1)
    text2_length = len(text2)

    dp = [[0] * (text2_length + 1) for _ in range(text1_length + 1)]
    ans_index = 0
    ans_length = 0

    for i in range(1, text1_length + 1):
        for j in range(1, text2_length + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
                if dp[i][j] > ans_length:
                    ans_index = i
                    ans_length = dp[i][j]

    return text1[ans_index - ans_length : ans_index]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
