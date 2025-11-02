# Problem 3289
import collections
from typing import List


class TheTwoSneakyNumsOfDigitville:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        cntr = collections.Counter(nums)
        return [k for k, v in cntr.items() if v > 1]
