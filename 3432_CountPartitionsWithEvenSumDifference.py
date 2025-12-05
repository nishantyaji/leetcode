# Problem 3432
import itertools
from typing import List


class CountPartitionsWithEvenSumDifference:
    def countPartitions(self, nums: List[int]) -> int:
        l = list(itertools.accumulate(nums))[:-1]
        r = list(itertools.accumulate(nums[::-1]))[:-1][::-1]
        res = 0
        for i in range(len(l)):
            if l[i] % 2 == r[i] % 2:
                res += 1
        return res