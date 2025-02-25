# Problem 1524
import itertools
from typing import List


class NumOfSubarrayWithOddSum:

    def numOfSubarrays(self, arr: List[int]) -> int:
        even, odd, res, base = 1, 0, 0, 1000000007
        prefix = list(itertools.accumulate(arr))
        for i, a in enumerate(prefix):
            if a % 2 == 1:
                res = (res + even) % base
                odd += 1
            else:
                res = (res + odd) % base
                even += 1
        return res


if __name__ == '__main__':
    n = NumOfSubarrayWithOddSum()
    print(n.numOfSubarrays([1, 3, 5]))
    print(n.numOfSubarrays([2, 4, 6]))
    print(n.numOfSubarrays([1, 2, 3, 4, 5, 6, 7]))
