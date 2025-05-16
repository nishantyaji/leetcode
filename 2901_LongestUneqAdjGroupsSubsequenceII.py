import collections
from typing import List


class LongestUneqAdjGroupsSubsequenceII:

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
            if max(dp[i]) > 2:
                return 2

        return max(dp[-1])

    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:

        def hamming(w1: str, w2: str):
            if abs(len(w2) - len(w1)) >= 2:
                return 2
            if len(w1) == len(w2):
                l = 0
                for i in range(len(w1)):
                    l += (0 if w1[i] == w2[i] else 1)
                return l
            else:
                temp_len = self.longestCommonSubsequence(w1, w2)
                return len(w1) + len(w2) - temp_len

        adj = collections.defaultdict(list)
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if hamming(words[i], words[j]) == 1 and groups[i] != groups[j]:
                    adj[i].append(j)

        all_visit, max_map, res = set(),  {}, {"value": [0]}

        for i in range(len(groups)):
            if i in all_visit:
                continue

            def dfs(nod, visi):
                res_arr = [nod]
                for nei in adj[nod]:
                    if nei not in all_visit:
                        all_visit.add(nod)
                        res_temp = [nod] + dfs(nei, visi)
                    else:
                        res_temp = [nod] + max_map[nei]

                    if len(res_temp) > len(res_arr):
                        res_arr = res_temp
                    max_map[nod] = res_arr
                return res_arr

            local_vis = {i}
            res_outer = dfs(i, local_vis)
            if len(res_outer) > len(res["value"]):
                res["value"] = res_outer
        return list(map(lambda i: words[i], res["value"]))


if __name__ == '__main__':
    l = LongestUneqAdjGroupsSubsequenceII()
    print(l.getWordsInLongestSubsequence(["bcb","bab","bcc","ca","bb","db","bd","daa","da","dc","aaa","dd","abb","cd","bdc"],
                                         [4,9,4,8,6,7,11,11,9,12,12,10,10,12,15]))   #  ["bb","db","da","dc","dd","cd"]
