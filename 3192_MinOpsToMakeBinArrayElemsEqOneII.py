# Problem 3192
from typing import List


class MinOpsToMakeBinArrayElemsEqOneII:
    def minOperations(self, nums: List[int]) -> int:
        result = 0
        for i in range(len(nums)):
            if (result + nums[i]) % 2 == 0:
                result += 1
        return result
