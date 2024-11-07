# Problem 2275
import collections
from typing import List


class LargestCombinationBitwiseAndGTZero:
    def largestCombination(self, candidates: List[int]) -> int:
        cntr = collections.Counter()
        for c in candidates:
            bstr = format(c, "b")
            base = 1
            for i in bstr[::-1]:
                if i == "1":
                    cntr[base] += 1
                base = base << 1
        return max(cntr.values())
