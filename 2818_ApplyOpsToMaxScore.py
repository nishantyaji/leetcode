# Problem 2818
import functools
import heapq
import math
from typing import List


class ApplyOpsToMaxScore:

    @functools.cache
    def primes_list(self, numm: int) -> List[int]:
        flags = [True] * (numm + 1)
        flags[0] = False
        flags[1] = False
        for i in range(2, 1 + int(math.sqrt(numm))):
            if flags[i]:
                for j in range(2, 1 + numm // i):
                    if i * j <= numm:
                        flags[i * j] = False

        return [i for i, x in enumerate(flags) if x]

    def prime_score(self, numm: int, primes: List[int]) -> int:
        if numm == 1:
            return 0
        score = 0
        for p in primes:
            flag = False
            while numm % p == 0:
                numm = numm // p
                flag = True
            if flag:
                score += 1
            if numm == 1:
                return score
        return score

    def occurrences(self, ps: List[int], base: int) -> List[tuple]:
        pslen = len(ps)
        occ, lstack = [(0, 0)] * pslen, []
        left, right = [0] * pslen, [0] * pslen
        for i, x in enumerate(ps):
            # stack has (index, value)
            while lstack and lstack[-1][1] < x:
                pop_idx, pop_val = lstack.pop()
                right[pop_idx] += (i - pop_idx - 1)
            if not lstack:
                left[i] += i
            else:
                left[i] += (i - lstack[-1][0] - 1)
            lstack.append((i, x))

        while lstack:
            pop_idx, pop_val = lstack.pop()
            right[pop_idx] += (pslen - pop_idx - 1)

        for i in range(pslen):
            occ[i] = ((left[i] + 1), (right[i] + 1))
        return occ

    def fast_pow(self, val: int, t: int, base: int):
        if t > base:
            q, r = divmod(t, base - 1)
            return self.fast_pow(val, r, base)

        res = 1
        mult = val
        while t > 0:
            if t & 1 == 1:
                res = (mult * res) % base
            mult = (mult * mult) % base
            t = t >> 1
        return res

    def maximumScore(self, nums: List[int], k: int) -> int:
        base = 1000000007
        # primes = self.primes_list(max(nums))
        # ps = [self.prime_score(n, primes) for n in nums]
        # For some reason,
        # calculating and caching primes beforehand (through sieve)
        # and then calculating prime score is slower
        # than calculating prime score without sieve and caching.
        # Very counterintuitive. Spent many hours on this
        ps = [0] * len(nums)
        for i, n in enumerate(nums):
            prime_score = 0
            for j in range(2, int(math.sqrt(n)) + 1):
                flag = False
                while n % j == 0:
                    flag = True
                    n = n // j
                if flag:
                    prime_score += 1
            if n >= 2:
                prime_score += 1
            ps[i] = prime_score

        occ = self.occurrences(ps, base)
        pq = [(-n, occ[i][0], occ[i][1]) for i, n in enumerate(nums)]
        heapq.heapify(pq)

        score = 1
        while k > 0:
            val, l, r = heapq.heappop(pq)
            temp = l * r
            val, t = -val, min(temp, k)
            score = (score * (pow(val, t, base))) % base
            k -= t
        return score % base

if __name__ == '__main__':
    a = ApplyOpsToMaxScore()
    print(a.maximumScore([8, 3, 9, 3, 8], 2))  # 81
    print(a.maximumScore([1, 7, 11, 1, 5], 14))  # 823751938
    print(a.maximumScore([3289, 2832, 14858, 22011], 6))  # 256720975
    print(a.maximumScore([19, 12, 14, 6, 10, 18], 3))  # 4788
