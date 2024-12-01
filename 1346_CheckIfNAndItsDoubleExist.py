# Problem 1346
import collections
from typing import List


class CheckIfNAndItsDoubleExist:
    def checkIfExist(self, arr: List[int]) -> bool:
        cntr = collections.Counter(arr)
        return cntr[0] >= 2 or any([2 * a in cntr for a in arr if a != 0])
