# Problem 1800
from typing import List


class MaxAscendingSubarraySum:
    def maxAscendingSum(self, nums: List[int]) -> int:
        prev, cumu, res = -1, 0, -1
        for i in range(0, len(nums)):
            res = max(cumu, res)
            if nums[i] > prev:
                cumu += nums[i]
            else:
                cumu = nums[i]
            prev = nums[i]
        return max(cumu, res)
