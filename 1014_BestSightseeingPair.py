# Problem 1014
import itertools
import sys
from typing import List


class BestSightseeingPair:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        vals = [i + x for i, x in enumerate(values)]
        max_vals = list(itertools.accumulate(vals, max))
        res = -sys.maxsize
        for i in range(1, len(vals)):
            res = max(res, max_vals[i - 1] + values[i] - i)
        return res

