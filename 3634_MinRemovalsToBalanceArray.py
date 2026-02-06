# Problem 3634
import sys
from bisect import bisect
from typing import List


class MinRemovalsToBalanceArray:
    def minRemoval(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return 0
        nums.sort()
        mn = sys.maxsize
        for i in range(len(nums) - 1):
            res = i
            r = bisect.bisect_right(nums, k * nums[i])
            res += (len(nums) - r)
            mn = min(mn, res)
        return mn