# Problem 476
import math


class NumberComplement:
    def findComplement(self, num: int) -> int:
        if num == 1:
            return 0
        pw = (int(math.log2(num))) + 1
        return (2 ** pw) - 1 - num
