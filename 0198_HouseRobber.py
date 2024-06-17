# Problem 198
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums)
        dp[0], dp[1] = nums[0], nums[1]
        this_max = max(dp)
        for index, n in enumerate(nums[2:]):
            dp[index + 2] = n + dp[index]
            if index - 1 >= 0:
                dp[index + 2] = max(dp[index + 2], n + dp[index - 1])
            this_max = max(this_max, dp[index + 2])
        return this_max
