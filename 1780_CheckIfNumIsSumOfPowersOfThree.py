# Problem 1780
import math


class CheckIfNumIsSumOfPowersOfThree:

    def checkPowersOfThree(self, n: int) -> bool:

        p = int(math.log(n) / math.log(3))
        r = n
        while p >= 1:
            q, r = divmod(n, 3 ** p)
            if q == 2:
                return False
            p, n = p - 1, r
        if r == 2:
            return False
        return True
