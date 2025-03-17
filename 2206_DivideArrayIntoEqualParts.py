# Problem 2206
import collections
from typing import List


class DivideArrayIntoEqualParts:
    def divideArray(self, nums: List[int]) -> bool:
        counter = collections.Counter(nums)
        for _, v in counter.items():
            if v % 2 == 1:
                return False
        return True
