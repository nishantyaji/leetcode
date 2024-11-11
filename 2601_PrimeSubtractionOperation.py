# Problem 2601
import bisect
import functools
import math
from typing import List


class PrimeSubtractionOperation:

    @functools.cache
    def get_primes(self):
        limit = 1001
        sq_l = math.ceil(math.sqrt(limit))
        flags = [True] * limit
        flags[0] = False
        flags[1] = False
        flags[2] = True
        for i in range(2, sq_l):
            if flags[i]:
                for j in range(2, math.ceil(limit / i)):
                    if i * j < limit:
                        flags[i * j] = False

        return [i for i, x in enumerate(flags) if x]

    def primeSubOperation(self, nums: List[int]) -> bool:
        primes = self.get_primes()

        idx = bisect.bisect_left(primes, nums[0])
        if idx > 0:
            nums[0] -= primes[idx - 1]
        diff = nums[0]

        for i in range(1, len(nums)):
            to_find = nums[i] - diff
            idx = bisect.bisect_left(primes, to_find)
            to_subtract = 0 if idx == 0 else primes[idx - 1]
            if idx == 0 and nums[i] <= nums[i - 1]:
                return False
            nums[i] = nums[i] - to_subtract
            diff = nums[i]
        return True


if __name__ == '__main__':
    p = PrimeSubtractionOperation()
    print(p.primeSubOperation([998, 2]))
    print(p.primeSubOperation([4, 9, 6, 10]))
    print(p.primeSubOperation([6, 8, 11, 12]))
    print(p.primeSubOperation([5, 8, 3]))
