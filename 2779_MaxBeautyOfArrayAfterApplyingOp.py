import bisect
import collections
from typing import List


class MaxBeautyOfArrayAfterApplyingOp:

    def maximumBeauty(self, nums: List[int], k: int) -> int:
        # Line sweep application
        if len(nums) == 1:
            return 1
        dp = [0] * 100002
        mx = -1
        for n in nums:
            dp[max(0, n - k)] += 1
            dp[min(100001, n + k + 1)] -= 1
            mx = max(mx, n)

        res, run_sum = 0, 0
        for i in range(0, mx + 1):
            run_sum += dp[i]
            res = max(res, run_sum)
        return res

    def maximumBeauty3(self, nums: List[int], k: int) -> int:
        # using window/deque
        nums.sort()
        res = -1
        right = bisect.bisect_right(nums, nums[0] + k)
        dq = collections.deque()
        for x in range(0, right):
            dq.append(nums[x])
        x = nums[0]
        while x <= nums[-1]:
            res = max(res, len(dq))
            x += 1
            while dq and dq[0] < x - k:
                dq.popleft()
            while right < len(nums) and nums[right] <= x + k:
                dq.append(nums[right])
                right += 1
        res = max(res, len(dq))
        return res

    def maximumBeauty2(self, nums: List[int], k: int) -> int:
        # using binary search
        nums.sort()
        res = -1
        for n in range(nums[0], nums[-1] + 1):
            lIdx = bisect.bisect_left(nums, n - k)
            rIdx = bisect.bisect_right(nums, n + k)
            res = max(res, rIdx - lIdx)
        return res


if __name__ == '__main__':
    m = MaxBeautyOfArrayAfterApplyingOp()
    print(m.maximumBeauty([13, 46, 71], 29))
    print(m.maximumBeauty([12, 71], 10))
