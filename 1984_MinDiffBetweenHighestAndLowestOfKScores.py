# Problem 1984
import sys
from typing import List


class MinDiffBetweenHighestAndLowestOfKScores:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        res = sys.maxsize
        for i in range(0, len(nums) - k + 1):
            res = min(res, nums[i] - nums[i + k - 1])

        return res
