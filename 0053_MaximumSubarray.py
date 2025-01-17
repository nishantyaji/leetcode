# Problem 53
import sys
from typing import List


class MaximumSubarray:
    def maxSubArray(self, nums: List[int]) -> int:
        return self.kadane(nums)

    def kadane(self, arr: List[int]) -> int:
        run_sum, min_till, max_sum = 0, 0, -sys.maxsize
        for x in arr:
            run_sum += x
            max_sum = max(max_sum, run_sum - min_till)
            min_till = min(min_till, run_sum)
        return max_sum
