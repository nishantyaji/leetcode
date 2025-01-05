# Problem 2270
from typing import List


class NumWaysToSplitArray:

    def waysToSplitArray(self, nums: List[int]) -> int:
        prefix, res, total = 0, 0, sum(nums)
        for x in nums[:-1]:
            prefix += x
            res += (1 if prefix >= total - prefix else 0)
        return res

