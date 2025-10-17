# Problem 2221
from typing import List


class FindTriangularSumOfArray:
    def triangularSum(self, nums: List[int]) -> int:
        def temp_fn(arr):
            res = []
            for i in range(len(arr) - 1):
                res.append((arr[i] + arr[i + 1]) % 10)
            return res

        while len(nums) > 1:
            nums = temp_fn(nums)
        return nums[0]
