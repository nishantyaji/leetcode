# Problem 2044
import functools
from typing import List


class CountNumMaxBitwiseORSubsets:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        res, target = [0], functools.reduce(lambda x, y: x | y, nums)
        self.recurse(nums, 0, res, target)
        return res[0]

    def recurse(self, remain: List[int], running: int, result: List[int], target: int):

        if remain:
            chosen = remain[0]
            if running | chosen == target:
                result[0] += 1
            if len(remain) > 1:
                self.recurse(remain[1:], running | chosen, result, target)
            self.recurse(remain[1:], running, result, target)
