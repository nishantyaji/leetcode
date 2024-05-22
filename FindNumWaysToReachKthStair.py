# Problem 3154. Find Number of Ways to Reach the K-th Stair

import math


class FindNumWaysToReachKthStair:

    def waysToReachStair(self, k: int) -> int:
        if k == 0:
            return 2
        if k == 1:
            return 4

        pow2 = int(math.log2(k - 1))
        result = 0
        for x in [pow2 - 1, pow2, pow2 + 1]:
            if pow(2, x + 1) - 1 - (x + 2) <= (k - 1) <= pow(2, x + 1):
                diff = pow(2, x + 1) - 1 - (k - 1)
                if 0 <= diff <= x + 2:
                    result += math.comb(x + 2, diff)
        return result


if __name__ == '__main__':
    w = FindNumWaysToReachKthStair()
    print(w.waysToReachStair(1013))
    print(w.waysToReachStair(2))
