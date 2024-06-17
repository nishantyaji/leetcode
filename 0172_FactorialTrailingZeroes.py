#Problem  172

import math


class FactorialTrailingZeroes:
    def trailingZeroes(self, n: int) -> int:
        if n < 5:
            return 0
        pow_highest = int(math.log(n, 5))
        result = 0

        for pow_highest in range(pow_highest, 0, -1):
            base = int(math.pow(5, pow_highest))
            result += int(n / base)
        return result
