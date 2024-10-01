# Problem 1497
import collections
from typing import List


class CheckIfPairsAreDivisibleByK:
    def canArrange(self, arr: List[int], k: int) -> bool:
        cntr = collections.Counter([a % k for a in arr])
        if k % 2 == 0:
            return cntr[k // 2] % 2 == 0 and cntr[0] % 2 == 0 and all(
                [v == cntr[k - a] for a, v in cntr.items() if a not in [k // 2, 0]])
        return cntr[0] % 2 == 0 and all([v == cntr[k - a] for a, v in cntr.items() if a != 0])