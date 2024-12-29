# Problem 1639
import collections
from typing import List


class NumWaysFormTargetStrGivenDictionary:

    def numWays(self, words: List[str], target: str) -> int:
        base = 1000000007
        cntr = collections.defaultdict(dict)
        for i in range(len(words[0])):
            this_dict = collections.defaultdict(int)
            for j in range(len(words)):
                this_dict[words[j][i]] += 1
            cntr[i] = this_dict

        # dp[index running][how many target chosen]
        dp = [[0 for _ in range(len(target) + 1)] for _ in range(len(words[0]))]
        dp[0][1] = cntr[0][target[0]]
        for i in range(1, len(words[0])):
            dp[i][1] = (dp[i-1][1] + cntr[i][target[0]]) % base
            for j in range(2, min(len(target), i+1) + 1):
                dp[i][j] = (dp[i-1][j] + dp[i-1][j-1] * cntr[i][target[j-1]]) % base
        return dp[-1][-1] % base


if __name__ == '__main__':
    n = NumWaysFormTargetStrGivenDictionary()
    print(n.numWays(["abcd"], "abcd"))
    print(n.numWays(["acca","bbbb","caca"], "aba"))
    print(n.numWays(["abba","baab"], "bab"))
