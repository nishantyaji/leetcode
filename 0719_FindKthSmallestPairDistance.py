# Problem 719
import bisect
import functools
from typing import List


class FindKthSmallestPairDistance:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        start, end, mp = 0, nums[-1], dict()

        @functools.cache
        def val_(mid: int):
            res = 0
            for i, n in enumerate(nums):
                m_idx = bisect.bisect_left(nums, n + mid + 1)
                res += (m_idx - 1 - i)
            return res

        visited = set()
        while start <= end:
            mid = (start + end) // 2
            if mid in visited and val_(mid) <= k < val_(mid + 1):
                return mid
            res = val_(mid)
            if res >= k:
                end = mid - 1
            else:
                start = mid + 1
        return start


if __name__ == '__main__':
    f = FindKthSmallestPairDistance()
    print(f.smallestDistancePair([1, 3, 1], 1), "=0")
    print(f.smallestDistancePair([9, 10, 7, 10, 6, 1, 5, 4, 9, 8], 18), "=2")
    print(f.smallestDistancePair([2, 2, 0, 1, 1, 0, 0, 1, 2, 0], 2), "=0")
    print(f.smallestDistancePair([1, 1, 1], 2), "=0")
    # print(f.smallestDistancePair([],))
