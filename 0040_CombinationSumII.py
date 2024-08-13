# Problem 40
import bisect
import collections
import copy
from typing import List


class CombinationSumII:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if sum(candidates) < target:
            return []
        res = []
        cntr = collections.Counter(candidates)
        if target in cntr:
            res.append([target])
        keys = list(cntr.keys())
        keys.sort()
        idx = bisect.bisect_left(keys, target)
        self.recurse(cntr, keys, idx, target, res, [])
        return res

    def recurse(self, cntr: dict, c: List[int], idx: int, target: int, res: List[List[int]], run: List[int]):
        if idx == -1 or target == 0:
            return

        for i in range(idx - 1, -1, -1):
            for mul in range(1, cntr[c[i]] + 1):
                rem = target - mul * c[i]
                if rem < 0:
                    break
                run_d = copy.deepcopy(run)
                run_d += ([c[i]] * mul)

                if rem == 0:
                    res.append(run_d)
                elif rem > 0:
                    self.recurse(cntr, c, i, rem, res, run_d)


if __name__ == '__main__':
    c = CombinationSumII()
    print(c.combinationSum2([1], 1))
    # [[1]]
    print(c.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
    # [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
    print(c.combinationSum2([2, 5, 2, 1, 2], 5))
    # [[1, 2, 2], [5]]
    print(c.combinationSum2([1], 2))
    # []
    print(c.combinationSum2([1, 1], 2))
    # [[1, 1]]
