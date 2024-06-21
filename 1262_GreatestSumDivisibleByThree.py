# Problem 1262

import math
from typing import List


class GreatestSumDivisibleByThree:
    def maxSumDivThree(self, nums: List[int]) -> int:
        min11, min12, min21, min22 = math.inf, math.inf, math.inf, math.inf
        total = 0
        for n in nums:
            total = total + n
            if n % 3 == 1:
                if n < min11:
                    min12 = min11
                    min11 = n
                elif n < min12:
                    min12 = n
            if n % 3 == 2:
                if n < min21:
                    min22 = min21
                    min21 = n
                elif n < min22:
                    min22 = n
        if total % 3 == 1:
            if min21 + min22 > min11:
                total -= min11
            else:
                if (min21 + min22) != math.inf:
                    total -= (min21 + min22)
        if total % 3 == 2:
            if min11 + min12 > min21:
                total -= min21
            else:
                if (min11 + min12) != math.inf:
                    total -= (min11 + min12)
        return total


if __name__ == '__main__':
    g = GreatestSumDivisibleByThree()
    print(g.maxSumDivThree([3, 6, 5, 1, 8]))
    print(g.maxSumDivThree([4]))
    print(g.maxSumDivThree([1, 2, 3, 4, 4]))
