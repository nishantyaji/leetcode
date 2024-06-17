# Problem 974
import collections
import itertools
import math
from typing import List


class SubarraySumDivisibleByK:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        #prefix sum
        nums = list(itertools.accumulate(nums))
        this_counter = collections.Counter(list(map(lambda x: x % k, nums + [0])))
        return sum([math.comb(v, 2) for k, v in this_counter.items() if v > 1])


if __name__ == '__main__':
    s = SubarraySumDivisibleByK()
    print(s.subarraysDivByK([4, 5, 0, -2, -3, 1], 5))
    print(s.subarraysDivByK([5], 9))
