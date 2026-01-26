# Problem 1200
import collections
import sys
from typing import List


class MinAbsDiff:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        d = collections.defaultdict(list)
        mn = sys.maxsize
        for i in range(1, len(arr)):
            diff = arr[i] - arr[i - 1]
            if diff < mn:
                mn = diff
            d[diff].append([arr[i - 1], arr[i]])
        return d[mn]
