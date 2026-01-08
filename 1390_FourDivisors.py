# Problem 1390
import functools
import math
from typing import List


class FourDivisors:
    def sumFourDivisors(self, nums: List[int]) -> int:
        mp = self.form_map()
        return sum([mp[x] if x in mp else 0 for x in nums])

    @functools.cache
    def form_map(self) -> int:
        primes = self.get_primes()
        mp = {}
        for p in primes:
            cube = p * p * p
            if cube > 100000:
                break
            mp[cube] = cube + p * p + p + 1

        for i in range(len(primes)):
            for j in range(i + 1, len(primes)):
                prod = primes[i] * primes[j]
                if prod > 100000:
                    break
                mp[prod] = prod + primes[i] + primes[j] + 1

        return mp

    @functools.cache
    def get_primes(self) -> list[int]:
        limit = 100001
        flag = [0 for _ in range(limit)]
        flag[0] = 1
        flag[1] = 1
        sq = int(math.sqrt(limit))
        for i in range(2, sq + 1):
            if flag[i] == 0:
                for j in range(2, limit // i + 1):
                    if i * j < limit:
                        flag[i * j] = 1
        res = [i for i, x in enumerate(flag) if x == 0]
        return res
