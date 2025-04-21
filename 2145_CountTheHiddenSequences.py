# Problem 2145
from typing import List


class CountTheHiddenSequences:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        n = len(differences) + 1
        run_sum, mn, mx = 0, 0, 0
        for i in range(n - 1):
            run_sum += differences[i]
            mn = min(mn, run_sum)
            mx = max(mx, run_sum)
        later = upper - mx
        before = lower - mn
        if before > later:
            return 0
        return later - before + 1
