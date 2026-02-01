# Problem 3010
from typing import List


class DivideAnArrayIntoSubarraysWithMinCostI:
    def minimumCost(self, nums: List[int]) -> int:
        res, nums = nums[0], nums[1:]
        nums.sort()
        return sum(nums[:2]) + res
