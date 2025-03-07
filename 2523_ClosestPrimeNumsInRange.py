# Problem 2523
import bisect
import functools
import sys
from typing import List


class ClosestPrimeNumsInRange:

    @functools.cache
    def get_primes(self) -> List[int]:
        limit = 1000000
        flag = [True] * (limit + 1)
        flag[0] = False
        flag[1] = False

        for i in range(2, 1001):
            if flag[i]:
                for j in range(2, int(limit / i) + 1):
                    if i * j <= limit:
                        flag[i * j] = False
        return [i for i, x in enumerate(flag) if x]

    def closestPrimes(self, left: int, right: int) -> List[int]:
        primes = self.get_primes()
        l_idx = bisect.bisect_left(primes, left)
        r_idx = bisect.bisect_right(primes, right)
        arr = primes[l_idx:r_idx]
        if len(arr) <= 1:
            return [-1, -1]
        pairs = [(arr[i + 1] - arr[i], arr[i]) for i in range(len(arr) - 1)]
        # pairs.sort(key=lambda x: (x[0], x[1]))  # O(n*logn)
        diff, res = sys.maxsize, [-1, -1]
        for p in pairs:
            if p[0] < diff:
                res = [p[1], p[1] + p[0]]
                diff = p[0]
        return res
