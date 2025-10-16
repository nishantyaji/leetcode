# Problem 3350
from typing import List


class AdjacentIncreasingSubarraysDetectionII:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        parity = [1 if nums[i] < nums[i + 1] else 0 for i in range(len(nums) - 1)]
        temp, cum, res = [], 0, 0
        for i in parity:
            if i == 0:
                temp.append(cum)
                cum = 0
            else:
                cum += 1

        temp.append(cum)
        for i in range(len(temp) - 1):
            if temp[i] > 0 and temp[i + 1] > 0:
                val = min(temp[i], temp[i + 1])
                res = max(val + 1, res)
        res = max(res, (max(temp) + 1) // 2)
        res = max(res, 1)
        return res
