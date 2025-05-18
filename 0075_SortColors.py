# Problem 75
import collections
from typing import List


class SortColors:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cntr, j = collections.Counter(nums), 0
        for i in [0, 1, 2]:
            while cntr[i] > 0:
                nums[j] = i
                j += 1
                cntr[i] -= 1
        return nums

