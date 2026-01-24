# Problem 1877
from typing import List


class MinMaxPairSumInArray:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return max(map(lambda i: nums[i] + nums[len(nums) - 1 - i], list(range(0, len(nums) // 2))))
