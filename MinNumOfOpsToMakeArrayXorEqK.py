# Problem 2997

from typing import List
import math


class MinNumOfOpsToMakeArrayXorEqK:
    def minOperations(self, nums: List[int], k: int) -> int:
        res = nums[0]
        nums.append(k)

        for i in range(1, len(nums)):
            res = res ^ nums[i]
        return self.count_one_bits(res)

    def count_one_bits(self, num: int) -> int:
        if num == 0 or num == 1:
            return num
        digits = int(math.log2(num)) + 1
        checker, result = 1, 0
        for i in range(0, digits):
            result = result + (1 if num & checker != 0 else 0)
            checker = checker << 1
        return result


if __name__ == '__main__':
    m = MinNumOfOpsToMakeArrayXorEqK()
    print(m.minOperations([2, 1, 3, 4], 1))
    print(m.minOperations([2, 0, 2, 0], 0))
