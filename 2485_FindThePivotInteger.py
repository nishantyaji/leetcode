# Problem 2485

import math

class FindThePivotInteger:

    def is_square(self, n: int):
        sq = int(math.sqrt(n))
        return sq * sq == n, sq

    def pivotInteger(self, n: int) -> int:
        if n == 1:
            return 1

        sigma = int((n * (n + 1)) / 2)
        is_sq, sq = self.is_square(sigma)
        if is_sq:
            return sq
        else:
            return -1
        
        
        