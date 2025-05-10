# Problem 2918
from typing import List


class MinEqSumOf2ArraysAfterReplacing0s:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        diff = sum(nums1) - sum(nums2)
        z1, z2 = sum([1 for x in nums1 if x == 0]), sum([1 for x in nums2 if x == 0])

        if z1 == 0 and z2 == 0:
            return sum(nums1) if diff == 0 else -1
        elif z1 == 0:
            if diff == 0 and z2 > 0:
                return -1
            elif diff < 0 or abs(diff) < z2:
                return -1
            else:
                return sum(nums1)
        elif z2 == 0:
            if diff == 0 and z1 > 0:
                return -1
            elif diff > 0 or abs(diff) < z1:
                return -1
            else:
                return sum(nums2)
        else:
            return max(sum(nums2) + z2, sum(nums1) + z1)
