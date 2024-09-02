# Problem 1894
import bisect
import itertools
from typing import List


class FindStudentWillReplaceChalk:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        k = k % sum(chalk)
        pref = list(itertools.accumulate(chalk))  # prefix sum
        return bisect.bisect_right(pref, k)
