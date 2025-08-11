# Problem 2438
import itertools
import math
import operator
from typing import List


class RangeProductQueriesOfPowers:

    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        limit, arr, ans = math.floor(math.log2(n)), [], []
        for i in range(limit, -1, -1):
            temp, r = divmod(n, pow(2, i))
            n = r
            if temp > 0:
                arr = [temp * pow(2, i)] + arr
        res = list(itertools.accumulate(arr, operator.mul))
        for [l, r] in queries:
            ans.append((res[len(res) - 1] if r >= len(res) - 1 else res[r]) // (res[l - 1] if l >= 1 else 1) % (1000000007))
        return ans


if __name__ == '__main__':
    r = RangeProductQueriesOfPowers()
    print(r.productQueries(13, [[1, 2], [1, 1]]))
    print(r.productQueries(15, [[0, 1], [2, 2], [0, 3]]))
    print(r.productQueries(2, [[0, 0]]))
