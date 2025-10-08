# Problem 3688
import functools
from typing import List


class BitwiseOrOfEvenNumbersInAnArray:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        return functools.reduce(lambda x, y: x | y, (map(lambda x: 0 if x % 2 == 1 else x, nums)), 0)
