# Problem 3512
from typing import List


class MinOpsToMakeArraySumDivisibleByK:

    def minOperations(self, nums: List[int], k: int) -> int:
        return sum(nums) % k