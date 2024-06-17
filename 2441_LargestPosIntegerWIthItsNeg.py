#Problem 2441

from typing import List

class LargestPosIntegerWithItsNeg:
    def findMaxK(self, nums: List[int]) -> int:
        neg_set = set()
        for n in nums:
            if n < 0:
                neg_set.add(n)
        nums.sort()

        for n in range(len(nums) - 1, -1, -1):
            if nums[n] < 0:
                break
            if -nums[n] in neg_set:
                return nums[n]
        return -1
