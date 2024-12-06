# Problem 2554
from typing import List


class MaxNumOfIntegersToChooseFromRangeI:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banset, count, total = set(banned), 0, 0
        for i in range(1, n + 1):
            if i in banset:
                continue
            total += i
            if total > maxSum:
                break
            count += 1
        return count
