# Problem 3375
import sys
from typing import List


class MinOpsToMakeArrayValuesEqK:
    def minOperations(self, nums: List[int], k: int) -> int:
        st, mn = set(), sys.maxsize
        for n in nums:
            st.add(n)
            mn = min(mn, n)

        return -1 if k > mn else len(st) - (k in st)
