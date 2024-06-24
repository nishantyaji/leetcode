# Problem 3191
from typing import List


class MinOpsToMakeBinArrayElemsEqOneI:
    def minOperations(self, nums: List[int]) -> int:
        return self.minKBitFlips(nums, 3)

    def minKBitFlips(self, nums: List[int], k: int) -> int:
        # My second approach which passed the muster
        # We go on flipping ints from left to right
        if k == 1:
            return sum(1 for n in nums if n == 0)

        result, i, run_sum = 0, 0, 0
        dq = [0] * k
        for i in range(len(nums) - k + 1):
            run_sum -= dq.pop(0)
            if (nums[i] + run_sum) % 2 == 0:
                dq.append(1)
                result += 1
                run_sum += 1
            else:
                dq.append(0)

        i += 1
        while i < len(nums):
            run_sum -= dq.pop(0)
            if (nums[i] + run_sum) % 2 == 0:
                return -1
            i += 1

        return result
