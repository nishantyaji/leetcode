# Problem 2419
from typing import List


class LongestSubArrayMaxBitwiseAnd:
    def longestSubarray(self, nums: List[int]) -> int:
        mx = max(nums)

        max_ln, ln = 0, 0
        for i in range(len(nums)):
            if nums[i] == mx:
                ln += 1
            else:
                ln = 0
            max_ln = max(ln, max_ln)
        return max_ln