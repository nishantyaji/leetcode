# Problem 1963
import itertools
import math
import operator
import sys


class MinNumSwapsMakeStrBalanced:
    def minSwaps(self, s: str) -> int:
        acc, min_ = 0, sys.maxsize
        for c in s:
            acc += (-1 if c == "]" else 1)
            min_ = min(min_, acc)
        return math.ceil(abs(min_) / 2)

    def minSwaps_oneliner(self, s: str) -> int:
        return math.ceil(abs(min(itertools.accumulate(map(lambda x: (-1 if x == "]" else 1), s), operator.add))) / 2)
