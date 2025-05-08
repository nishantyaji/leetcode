# Problem 1295
from typing import List


class FindNumWithEvenNumOfDigits:
    def findNumbers(self, nums: List[int]) -> int:
        return sum([1 if len(str(x)) % 2 == 0 else 0 for x in nums])
