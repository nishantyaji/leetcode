# Problem 2530
import heapq
import math
from typing import List


class MaxScoreAfterApplyingKOps:
    def maxKelements(self, nums: List[int], k: int) -> int:
        pq, res = [], 0
        heapq.heapify(pq)
        for n in nums:
            heapq.heappush(pq, -n)
        for _ in range(k):
            v = -heapq.heappop(pq)
            res += v
            heapq.heappush(pq, -math.ceil(v / 3))
        return res
