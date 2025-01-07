# Problem 1143

class LongestCommonSubsequence:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # This is a standard algo
        # Look up Levenshtein distance
        # The standard implementation is curt and cute
        a_set, b_set = set(list(text1)), set(list(text2))
        ixn = a_set.intersection(b_set)
        b, a = "".join([l for l in text2 if l in ixn]), "".join([l for l in text1 if l in ixn])
        dp = [[0 for _ in range(1 + len(b))] for _ in range(1 + len(a))]
        max_prev = [0] * (1 + len(b))

        for i in range(1, 1 + len(a)):
            for j in range(1, 1 + len(b)):
                if a[i - 1] == b[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], max_prev[j - 1])
                max_prev[j] = max(max_prev[j], max_prev[j - 1], dp[i][j])
        return max(dp[-1])
