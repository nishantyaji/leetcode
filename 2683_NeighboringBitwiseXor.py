# Problem 2683
import functools
import operator
from typing import List


class NeighboringBitwiseXor:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        return functools.reduce(operator.xor, derived) == 0
