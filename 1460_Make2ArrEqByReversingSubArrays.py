# Problem 1460
import collections
from typing import List


class Make2ArrEqByReversingSubArrays:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return len(collections.Counter(target) - collections.Counter(arr)) == 0
