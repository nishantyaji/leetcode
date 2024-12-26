# Problem 494
import itertools
from typing import List


class TargetSum:

    def __init__(self):
        self.nums = []
        self.suf_sum = []
        self.res = 0

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.res = 0
        self.nums = nums
        self.suf_sum = list(reversed(list(itertools.accumulate(reversed(nums)))))
        self.recurse(0, 0, target)
        return self.res

    def recurse(self, run_sum: int, index_on: int, target: int):
        # We can memoize this
        if index_on == len(self.nums):
            self.res += (1 if run_sum == target else 0)
            return
        suf = self.suf_sum[index_on]
        if run_sum - suf > target or run_sum + suf < target:
            return

        self.recurse(run_sum + self.nums[index_on], index_on + 1, target)
        self.recurse(run_sum - self.nums[index_on], index_on + 1, target)


if __name__ == '__main__':
    t = TargetSum()
    print(t.findTargetSumWays([1, 1, 1, 1, 1], 3))
    print(t.findTargetSumWays([1], 1))
    print(t.findTargetSumWays([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 1))
