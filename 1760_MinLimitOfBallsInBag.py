# Problem 1760
import bisect
import math
from typing import List


class MinLimitOfBallsInBag:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        if len(nums) == 1:
            q, r = divmod(nums[0], maxOperations + 1)
            return q + r
        nums.sort()

        s, e, res = 1, max(nums), -1
        while s <= e:
            mid = (s + e) // 2
            v = self.num_ops(nums, mid)
            if v <= maxOperations:
                res = mid
                e = mid - 1
            else:
                s = mid + 1

        return res

    def num_ops(self, nums: List[int], limit: int) -> int:

        idx = bisect.bisect_left(nums, limit)
        if idx > len(nums):
            return 0
        res = 0
        for i in range(idx, len(nums)):
            res += (math.ceil(nums[i] / limit) - 1)
        return res


if __name__ == '__main__':
    m = MinLimitOfBallsInBag()
    print(m.minimumSize([9], 2))
    print(m.minimumSize([2, 4, 8, 2], 4))
