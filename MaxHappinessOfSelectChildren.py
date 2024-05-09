# Problem 3075

from typing import List


class MaxHappinessOfSelectChildren:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        result = 0
        for i in range(0, k):
            result += max(happiness[i] - i, 0)
        return result
