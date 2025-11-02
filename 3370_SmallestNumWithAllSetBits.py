# Problem 3370
import math


class SmallestNumWithAllSetBits:

    def smallestNumber(self, n: int) -> int:
        return pow(2, math.ceil(math.log2(n + 1))) - 1