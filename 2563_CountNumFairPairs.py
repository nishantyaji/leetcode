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


if __name__ == '__main__':
    c = CountNumFairPairs()
    print(c.countFairPairs([0, 1, 7, 4, 4, 5], 3, 6))
    print(c.countFairPairs([1, 7, 9, 2, 5], 11, 11))
    print(c.countFairPairs([0, 0, 0, 0, 0, 0], 0, 0))
