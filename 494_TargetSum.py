# Problem 494
import functools
import itertools
from typing import List


class TargetSum:

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        suf_sum = list(reversed(list(itertools.accumulate(reversed(nums)))))

        @functools.cache
        def recurse(run: int, index: int) -> int:
            if index == len(nums):
                return 1 if run == target else 0
            if run - suf_sum[index] > target or run + suf_sum[index] < target:
                return 0
            plus = recurse(run + nums[index], index + 1)
            minus = recurse(run - nums[index], index + 1)
            return plus + minus

        return recurse(0, 0)


if __name__ == '__main__':
    t = TargetSum()
    print(t.findTargetSumWays([1, 1, 1, 1, 1], 3))
    print(t.findTargetSumWays([1], 1))
    print(t.findTargetSumWays([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 1))
