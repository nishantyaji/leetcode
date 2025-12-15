# Problem 2110
import sys
from typing import List


class NumOfSmoothDescentPeriodsOfStock:
    def getDescentPeriods(self, prices: List[int]) -> int:

        prev = -sys.maxsize
        counter = 1
        result = 0
        for i, x in enumerate(prices):
            if x == prev - 1:
                counter += 1
            else:
                if i > 0:
                    result = result + ((counter + 1) * counter) // 2
                counter = 1
            prev = x
        result = result + ((counter + 1) * counter) // 2
        return result
