# Problem 3190
from typing import List


class FindMinOpsToMakeAllElemsDivisibleBy3:

    def minimumOperations(self, nums: List[int]) -> int:
        return sum([1 if n % 3 != 0 else 0 for n in nums])
