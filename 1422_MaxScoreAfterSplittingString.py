# Problem 1422
import sys


class MaxScoreAfterSplittingString:
    def maxScore(self, s: str) -> int:
        res, zeroes, ones = -sys.maxsize, 0, 0
        for i, c in enumerate(s):
            if c == "0":
                zeroes += 1
            else:
                ones += 1
            if len(s) - 1 > i:
                res = max(res, zeroes - ones)
        return res + ones
