# Problem 2873
from typing import List


class MaxValueOfAnOrderedTripletI:
    def maximumTripletValue(self, nums: List[int]) -> int:

        arr = [0] * len(nums)
        res = 0
        mx = nums[-1]
        for i in range(len(nums) - 1, -1, -1):
            arr[i] = mx = max(mx, nums[i])
        print(arr)
        mx = nums[0]
        for i in range(1, len(nums) - 1):
            mx = max(mx, nums[i])
            res = max((mx - nums[i]) * arr[i + 1], res)
        return res
