# Problem 786

from typing import List
import functools


class KthSmallestPrimeFraction:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        #Implementation can be improved
        tuples = []

        def tup_comp(a, b):
            return a[0] * b[1] - a[1] * b[0]

        for i in range(0, len(arr) - 1):
            for j in range(i + 1, len(arr)):
                tuples.append((arr[i], arr[j]))

        tuples.sort(key=functools.cmp_to_key(tup_comp))
        return [tuples[k - 1][0], tuples[k - 1][1]]
