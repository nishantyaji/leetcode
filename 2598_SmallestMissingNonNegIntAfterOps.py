# Problem 2598
import collections
from typing import List


class SmallestMissingNonNegIntAfterOps:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        cntr = collections.Counter([n % value for n in nums])
        for i in range(value):
            if i not in cntr:
                return i
        mn = min(cntr.values())
        for i in range(value):
            if cntr[i] == mn:
                return mn * value + i
        return -1
