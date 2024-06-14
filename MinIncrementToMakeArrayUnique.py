# Problem 945
import math
from typing import List


class MinIncrementToMakeArrayUnique:

    def minOperations(self, nums: List[int]) -> int:
        # this is used by the O(NlogN) complexity
        result = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                result += (nums[i - 1] + 1 - nums[i])
                nums[i] = nums[i - 1] + 1
        return result

    def minIncrementForUnique2(self, nums: List[int]) -> int:
        # this is O(NlogN) time complexity
        nums.sort()
        return self.minOperations(nums)

    def minIncrementForUnique(self, nums: List[int]) -> int:
        # this is of O(2N) time complexity
        this_min, this_max, result, carry = math.inf, 0, 0, 0
        for n in nums:
            this_min, this_max = min(this_min, n), max(this_max, n)
        arr = [0] * (this_max - this_min + 1 + len(nums) - 1)
        for n in nums:
            arr[n - this_min] += 1
        for i in arr:
            if i > 1:
                carry += (i - 1)
            elif i == 0 and carry >= 1:
                carry -= 1
            result += carry
        return result


if __name__ == '__main__':
    m = MinIncrementToMakeArrayUnique()
    print(m.minIncrementForUnique([0]))
    print(m.minIncrementForUnique([1, 2, 2]))
    # 1
    print(m.minIncrementForUnique([3, 2, 1, 2, 1, 7]))
    # 6
