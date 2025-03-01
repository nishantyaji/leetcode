# Problem 2460
from typing import List


class ApplyOpsToArray:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            if nums[i + 1] == nums[i] and nums[i] != 0:
                nums[i] *= 2
                nums[i + 1] = 0
        res = [0] * len(nums)
        idx = 0
        for n in nums:
            if n != 0:
                res[idx] = n
                idx += 1
        return res
