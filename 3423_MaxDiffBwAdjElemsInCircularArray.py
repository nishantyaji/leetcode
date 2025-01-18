# Problem 3423
from typing import List


class MaxDiffBwAdjElemsInCircularArray:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 2:
            return abs(nums[0] - nums[1])
        mx = -1
        for i in range(n):
            mx = max(mx, abs(nums[i] - nums[(i + 1) % n]))
        return mx
