

class EditDistance:

    def __init__(self):
        self.word1 = ""
        self.word2 = ""
        self.dp = []

    def __min_dist_top_down_dp(self, m: int, n: int) -> int:
        if m == -1:
            return n + 1
        elif n == -1:
            return m + 1
        elif self.dp[m][n] > -1:
            return self.dp[m][n]
        else:
            if self.word1[m] == self.word2[n]:
                self.dp[m][n] = self.__min_dist_top_down_dp(m - 1, n - 1)
            else:
                insert = self.__min_dist_top_down_dp(m, n - 1)
                delete = self.__min_dist_top_down_dp(m - 1, n)
                replace = self.__min_dist_top_down_dp(m - 1, n - 1)
                self.dp[m][n] = 1 + min(insert, delete, replace)

            return self.dp[m][n]

    def min_dist_top_down(self, word1: str, word2: str) -> int:
        self.word1 = word1
        self.word2 = word2
        self.dp = [[-1 for _ in range(len(word2))] for _ in range(len(word1))]

        return self.__min_dist_top_down_dp(len(word1) - 1, len(word2) - 1)

    def min_dist_bottom_up(self, word1: str, word2: str) -> int:
        self.word1 = word1
        self.word2 = word2
        m = len(word1)
        n = len(word2)
        self.dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0:  
                    self.dp[i][j] = j
                elif j == 0:  
                    self.dp[i][j] = i
                elif word1[i - 1] == word2[j - 1]:  
                    self.dp[i][j] = self.dp[i - 1][j - 1]
                else:
                    insert = self.dp[i][j - 1]
                    delete = self.dp[i - 1][j]
                    replace = self.dp[i - 1][j - 1]
                    self.dp[i][j] = 1 + min(insert, delete, replace)
        return self.dp[m][n]


if __name__ == "__main__":
    solver = EditDistance()

    print("****************** Testing Edit Distance DP Algorithm ******************")
    print()

    S1 = input("Enter the first string: ").strip()
    S2 = input("Enter the second string: ").strip()

    print()
    print(f"The minimum edit distance is: {solver.min_dist_top_down(S1, S2)}")
    print(f"The minimum edit distance is: {solver.min_dist_bottom_up(S1, S2)}")
    print()
    print("*************** End of Testing Edit Distance DP Algorithm ***************")
