# Problem 2425
import functools
import operator
from typing import List


class BitwiseXorOfAllPairings:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        x1 = functools.reduce(operator.xor, nums1)
        x2 = functools.reduce(operator.xor, nums2)
        return (x1 if len(nums2) % 2 == 1 else 0) ^ (x2 if len(nums1) % 2 == 1 else 0)
