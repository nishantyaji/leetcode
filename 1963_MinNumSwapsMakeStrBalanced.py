# Problem 1963
import math
import sys


class MinNumSwapsMakeStrBalanced:
    def minSwaps(self, s: str) -> int:
        acc, min_ = 0, sys.maxsize
        for c in s:
            acc += (-1 if c == "]" else 1)
            min_ = min(min_, acc)
        return math.ceil(abs(min_) / 2)
