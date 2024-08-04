# Problem 1508
from typing import List


class RangeSumOfSortedSubArraySums:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sums = []
        for i in range(0, len(nums)):
            val = 0
            for j in range(i, len(nums)):
                val += nums[j]
                sums.append(val)
        sums.sort()
        return sum(sums[left - 1: right]) % (1000000000 + 7)
