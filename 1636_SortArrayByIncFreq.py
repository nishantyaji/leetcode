# Problem 1636
import collections
from functools import reduce
from typing import List


class SortArrayByIncFreq:
    def frequencySort(self, nums: List[int]) -> List[int]:
        return reduce(lambda acc, t: acc + [t[0]] * t[1],
                      sorted([(k, v) for k, v in collections.Counter(nums).items()], key=lambda t: (t[1], -t[0])), [])
