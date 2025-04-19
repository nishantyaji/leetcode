# Problem 2563

import bisect
from typing import List


class CountNumFairPairs:

    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        if len(nums) < 2 or lower > nums[-1] + nums[-2] or upper < nums[0] + nums[1]:
            return 0

        res = 0
        for i in range(len(nums)):
            l_idx = bisect.bisect_left(nums, lower - nums[i])
            u_idx = bisect.bisect_right(nums, upper - nums[i])
            if u_idx > l_idx:
                res += (u_idx - l_idx)
                if l_idx <= i < u_idx:
                    res -= 1
        return res // 2

    def countFairPairs_later_attempt(self, nums: List[int], lower: int, upper: int) -> int:
        mn = min(nums)
        if mn < 0:
            nums = [n + -mn for n in nums]
            lower += 2 * (-mn)
            upper += 2 * (-mn)

        nums.sort()
        mid = max(upper // 2, (lower + upper) // 2)
        mid_idx = bisect.bisect_right(nums, mid)
        res = 0
        for i in range(0, mid_idx):
            idx1 = bisect.bisect_right(nums, upper - nums[i])
            idx2 = max(i + 1, bisect.bisect_left(nums, lower - nums[i]))
            if idx1 >= idx2:
                res += (idx1 - idx2)
        return res


if __name__ == '__main__':
    c = CountNumFairPairs()
    print(c.countFairPairs([0, 1, 7, 4, 4, 5], 3, 6))
    print(c.countFairPairs([1, 7, 9, 2, 5], 11, 11))
    print(c.countFairPairs([0, 0, 0, 0, 0, 0], 0, 0))
