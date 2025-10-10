# Problem 2300
import bisect
from typing import List


class SuccessfulPairsOfSpellsAndPotions:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        res, n = [], len(potions)
        for s in spells:
            val = success / s
            idx = bisect.bisect_left(potions, val)
            res.append(n - idx)
        return res