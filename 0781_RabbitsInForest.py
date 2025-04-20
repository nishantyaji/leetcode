# Problem 781
import collections
import math
from typing import List


class RabbitsInForest:

    def numRabbits(self, answers: List[int]) -> int:
        cntr = collections.Counter(answers)
        res = 0
        for ans, occ in cntr.items():
            if occ > ans + 1:
                res += ((math.ceil(occ / (ans + 1))) * (ans + 1))
            else:
                res += (ans + 1)
        return res
