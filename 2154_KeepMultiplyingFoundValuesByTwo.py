# Problem 2154
from typing import List


class KeepMultiplyingFoundValuesByTwo:

    def findFinalValue(self, nums: List[int], original: int) -> int:
        s = set(nums)
        while original in s:
            original *= 2
        return original
