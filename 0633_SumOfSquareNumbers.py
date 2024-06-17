# Problem 633
import math


class SumOfSquareNumbers:
    def judgeSquareSum(self, c: int) -> bool:
        if c == 0:
            return True
        if c % 2 == 1 and c % 8 not in [1, 5]:
            return False
        sqc = int(math.sqrt(c))

        def is_square(n: int) -> bool:
            sq = int(math.sqrt(n))
            return sq * sq == n

        for i in range(1, sqc + 1):
            if is_square(c - (i * i)):
                return True
        return False
