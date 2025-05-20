import itertools
from typing import List


class ZeroArrayTransformationI:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        cum = [0] * (len(nums) + 1)
        for q in queries:
            cum[q[0]] += 1
            cum[q[1] + 1] -= 1
        comp = list(itertools.accumulate(cum))
        for i in range(len(nums)):
            if nums[i] > comp[i]:
                return False
        return True
