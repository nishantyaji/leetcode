# Problem 1590

import bisect
import collections
import functools
import operator
import sys
from typing import List


class MakeSumDivisibleByP:

    def minSubarray(self, nums: List[int], p: int) -> int:
        # Better approach. Time complexity : O(n)
        all_sum = functools.reduce(operator.add, nums)
        if all_sum % p == 0:
            return 0

        dp = {0: -1}
        to_remove = all_sum % p
        prefix = 0
        res = sys.maxsize
        for i in range(0, len(nums)):
            prefix += nums[i]
            compl = (prefix - to_remove) % p
            if compl in dp:
                res = min(res, i - dp[compl])
            dp[prefix % p] = i

        return -1 if res in [sys.maxsize, len(nums)] else res

    def minSubarray2(self, nums: List[int], p: int) -> int:
        # sub-optimal approach
        # O(nlogn) time complexity
        all_sum = functools.reduce(operator.add, nums)
        if all_sum % p == 0:
            return 0

        dp = collections.defaultdict(list)
        lenn = len(nums)

        suffix = 0
        first_pdiv_idx = -1
        for i in range(lenn - 1, -1, -1):
            suffix = (suffix + nums[i]) % p
            if suffix == 0:
                first_pdiv_idx = i
            dp[suffix].append(i)

        for k in dp.keys():
            dp[k] = dp[k][::-1]

        prefix = 0
        min_val = sys.maxsize
        last_pdiv_idx = -1
        for i in range(0, lenn):
            prefix = (prefix + nums[i]) % p
            if prefix == 0:
                last_pdiv_idx = i
            temp = dp[p - prefix]
            idx = bisect.bisect_right(temp, i)
            if idx < len(temp):
                min_val = min(min_val, temp[idx] - i - 1)

        if min_val == sys.maxsize:
            if last_pdiv_idx > -1:
                min_val = lenn - (last_pdiv_idx + 1)
            if first_pdiv_idx > - 1:
                min_val = min(min_val, first_pdiv_idx)

        if min_val == sys.maxsize:
            min_val = - 1

        return min_val


if __name__ == '__main__':
    m = MakeSumDivisibleByP()
    print(m.minSubarray([1, 2, 3], 7))
    print(m.minSubarray([3, 1, 4, 2], 6))
    print(m.minSubarray([6, 3, 5, 2], 9))
    print(m.minSubarray([1, 2, 3], 3))
