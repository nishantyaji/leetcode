# Problem 3191
import collections
from typing import List


class MinOpsToMakeBinArrayElemsEqOneI:

    def minOperations(self, nums: List[int]) -> int:
        # My new approach when I retried this after many months
        dq = collections.deque()
        dq.append(nums[0])
        dq.append(nums[1])

        res = 0
        for i in range(2, len(nums)):
            dq.append(nums[i])
            if dq[0] == 0:
                res += 1
                dq[1] = 1 ^ dq[1]
                dq[2] = 1 ^ dq[2]
            dq.popleft()

        return res if dq[0] == 1 and dq[1] == 1 else -1

    # -------------------------------------------------------

    def minOperations(self, nums: List[int]) -> int:
        return self.minKBitFlips(nums, 3)

    def minKBitFlips_before(self, nums: List[int], k: int) -> int:
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
