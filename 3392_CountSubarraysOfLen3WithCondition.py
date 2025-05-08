# Problem 3392
from typing import List


class CountSubarraysOfLen3WithCondition:
    def countSubarrays(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums) - 2):
            if nums[i + 1] == 2 * (nums[i] + nums[i + 2]):
                res += 1
        return res
