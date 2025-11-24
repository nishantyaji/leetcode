# Problem 1018
from typing import List


class BinaryPrefixDivisibleBy5:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res, temp = [], 0
        for n in nums:
            temp = 2 * temp + n
            res.append(temp % 5 == 0)
        return res
