# Problem 2740
from typing import List


class FindValueOfPartition:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()
        return min([nums[i] - nums[i - 1] for i in range(1, len(nums))])