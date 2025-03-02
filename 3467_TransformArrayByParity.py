# Problem 3467
from typing import List


class TransformArrayByParity:
    def transformArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        even = sum([1 for n in nums if n % 2 == 0])
        odd = n - even
        return [0] * even + [1] * odd
