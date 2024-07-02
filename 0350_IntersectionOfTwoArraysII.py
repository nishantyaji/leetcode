import collections
from typing import List


class IntersectionOfTwoArraysII:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter1 = collections.Counter(nums1)
        counter2 = collections.Counter(nums2)

        result = []
        for k, v in counter2.items():
            if k in counter1:
                v_min = min(v, counter1[k])
                result += [k] * v_min
        return result
