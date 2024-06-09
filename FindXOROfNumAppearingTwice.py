# 3158. Find the XOR of Numbers Which Appear Twice
import collections
import functools
from typing import List


class FindXOROfNumAppearingTwice:

    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        return functools.reduce(lambda x, y: x ^ y, [k for k, v in collections.Counter(nums).items() if v == 2], 0)


if __name__ == '__main__':
    b = FindXOROfNumAppearingTwice()
