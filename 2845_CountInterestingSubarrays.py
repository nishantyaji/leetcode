# Problem 2845
import collections
from typing import List


class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        nums2 = [1 if n % modulo == k else 0 for n in nums]
        return self.find_sol(nums2, modulo, k)

    def find_sol(self, arr: List[int], modulo: int, k: int) -> int:
        run_sum, res, cntr = 0, 0, collections.Counter()
        cntr[0] = 1
        for i in range(len(arr)):
            run_sum = (run_sum + arr[i]) % modulo
            res += cntr[(run_sum - k) % modulo]
            cntr[run_sum] += 1
        return res
