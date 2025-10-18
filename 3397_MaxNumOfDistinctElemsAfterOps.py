# Problem 3397
from typing import List


class MaxNumOfDistinctElemsAfterOps:

    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        avail = nums[0] - k + 1
        res = 1
        for n in nums[1:]:
            if abs(avail - n) <= k:
                res += 1
                avail += 1
            elif n - k > avail:
                res += 1
                avail = n - k + 1
        return res
