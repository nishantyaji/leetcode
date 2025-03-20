# Problem 3488
import bisect
import collections
from typing import List


class ClosestEqElementQueries:

    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        d = collections.defaultdict(list)
        for i, n in enumerate(nums):
            d[n].append(i)

        def dist(a, b):
            if b >= a:
                return [b - a, len(nums) - b + a]
            else:
                return [a - b, len(nums) - a + b]

        res = []
        for q in queries:
            l = d[nums[q]]
            ln = len(l)
            if ln == 1:
                res.append(-1)
            elif ln == 2:
                res.append(min(dist(l[0], l[1])))
            else:
                idx = bisect.bisect_left(l, q)
                before, after = l[(idx - 1) % ln], l[(idx + 1) % ln]
                res.append(min(dist(before, q) + dist(after, q)))
        return res
