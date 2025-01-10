# Refer problem 1143
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


# Function to find lcs_algo

def lcs_algo(S1, S2, m, n):
    # https://www.programiz.com/dsa/longest-common-subsequence
    L = [[0 for x in range(n + 1)] for x in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif S1[i - 1] == S2[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    index = L[m][n]
    lcs_algo = [""] * (index + 1)
    lcs_algo[index] = ""
    i, j = m, n
    while i > 0 and j > 0:
        if S1[i - 1] == S2[j - 1]:
            lcs_algo[index - 1] = S1[i - 1]
            i -= 1
            j -= 1
            index -= 1

        elif L[i - 1][j] > L[i][j - 1]:
            i -= 1
        else:
            j -= 1

    # Printing the sub-sequences
    print("S1 : " + S1 + "\nS2 : " + S2)
    print("LCS: " + "".join(lcs_algo))


S1 = "ACADB"
S2 = "CBDA"
m = len(S1)
n = len(S2)
lcs_algo(S1, S2, m, n)
