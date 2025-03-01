# Problem 1092

class ShortestCommonSupersequence:

    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        common = self.lcs_algo(str1, str2, len(str1), len(str2))
        res, idx_1, idx_2 = [], 0, 0
        for i in range(len(common)):
            while str1[idx_1] != common[i]:
                res += str1[idx_1]
                idx_1 += 1
            while str2[idx_2] != common[i]:
                res += str2[idx_2]
                idx_2 += 1
            res += common[i]
            idx_1 += 1
            idx_2 += 1
        while idx_1 < len(str1):
            res += str1[idx_1]
            idx_1 += 1
        while idx_2 < len(str2):
            res += str2[idx_2]
            idx_2 += 1
        return "".join(res)

    def lcs_algo(self, S1, S2, m, n):
        # https://www.programiz.com/dsa/longest-common-subsequence
        L = [[0 for x in range(n + 1)] for y in range(m + 1)]

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

        return "".join(lcs_algo)

    def shortestCommonSupersequence_MLE(self, str1: str, str2: str) -> str:
        cache = {}
        ans = self.recur(str1, str2, cache)
        return ans

    def recur(self, s1, s2, cache: dict) -> str:
        ss = [s1, s2]
        ss.sort()
        s1, s2 = ss[0], ss[1]
        if (s1, s2) in cache:
            return cache[(s1, s2)]
        if not s1 and not s2:
            cache[(s1, s2)] = ""
            return ""
        if not s1:
            cache[(s1, s2)] = s2[0] + self.recur(s1, s2[1:], cache)
            return cache[(s1, s2)]
        if not s2:
            cache[(s1, s2)] = s1[0] + self.recur(s1[1:], s2, cache)
            return cache[(s1, s2)]

        if s1[0] == s2[0]:
            cache[(s1, s2)] = s1[0] + self.recur(s1[1:], s2[1:], cache)
            return cache[(s1, s2)]
        temp1 = s1[0] + self.recur(s1[1:], s2, cache)
        temp2 = s2[0] + self.recur(s1, s2[1:], cache)

        if len(temp1) < len(temp2):
            cache[(s1, s2)] = temp1
            return temp1
        else:
            cache[(s1, s2)] = temp2
            return temp2

if __name__ == '__main__':
    s = ShortestCommonSupersequence()
    print(s.shortestCommonSupersequence("abac", "cab"))
    print(s.shortestCommonSupersequence("aaaaaaaa", "aaaaaaaa"))
