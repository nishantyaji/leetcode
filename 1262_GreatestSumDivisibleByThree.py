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

    def maxSumDivThree2(self, nums: List[int]) -> int:
        res = 0
        ones = []
        twos = []
        nums.sort()
        for n in nums:
            if n % 3 == 0:
                res += n
            elif n % 3 == 1:
                ones.append(n)
            else:
                twos.append(n)
        overall = sum(nums)
        if overall % 3 == 0:
            return overall
        if overall % 3 == 1:
            if not ones:
                return overall - twos[0] - twos[1]
            if not twos:
                return overall - ones[0]
            else:
                if len(twos) <= 1 or ones[0] < twos[0] + twos[1]:
                    return overall - ones[0]
                else:
                    return overall - twos[0] - twos[1]
        else:
            if not ones:
                return overall - twos[0]
            if not twos:
                return overall - ones[0] - ones[1]
            else:

                if len(ones) <= 1 or ones[0] + ones[1] > twos[0]:
                    return overall - twos[0]
                else:
                    return overall - ones[0] - ones[1]

if __name__ == '__main__':
    g = GreatestSumDivisibleByThree()
    print(g.maxSumDivThree([3, 6, 5, 1, 8]))
    print(g.maxSumDivThree([4]))
    print(g.maxSumDivThree([1, 2, 3, 4, 4]))
