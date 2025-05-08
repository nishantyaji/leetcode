# Problem 1128
import collections
from typing import List


class NumOfEquivalentDominoPairs:

    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        temp = [sorted(x) for x in dominoes]
        cntr = collections.Counter([(t[0], t[1]) for t in temp])
        res = 0
        for _, v in cntr.items():
            res += (((v - 1) * v) // 2)
        return res
