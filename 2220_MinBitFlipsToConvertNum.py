# Problem 2220

import math


class MinBitFlipsToConvertNum:
    def minBitFlips(self, start: int, goal: int) -> int:
        return self.count_one_bits(start ^ goal)

    def count_one_bits(self, num: int) -> int:
        # This is sub-optimal. Better ways of doing this
        # 1 better way is : return sum(list(map(int, bin(num)[2:])))
        if num == 0 or num == 1:
            return num
        digits = int(math.log2(num)) + 1
        checker, result = 1, 0
        for i in range(0, digits):
            result = result + (1 if num & checker != 0 else 0)
            checker = checker << 1
        return result
