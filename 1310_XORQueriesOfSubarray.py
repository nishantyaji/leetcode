# Problem 1310
import itertools
import operator
from typing import List


class XORQueriesOfSubarray:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        result = list(itertools.accumulate(arr, operator.xor))
        res = []
        for [l, r] in queries:
            if l == 0:
                res.append(result[r])
                continue
            res.append(result[r] ^ result[l - 1])
        return res
