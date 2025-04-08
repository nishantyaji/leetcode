# Problem 3396
import math
from typing import List


class MinNumOfOpsToMakeElemsInArrayDistinct:

    def minimumOperations(self, nums: List[int]) -> int:
        st, idx = set(), -1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] not in st:
                st.add(nums[i])
            else:
                idx = i
                break
        return math.ceil((idx + 1) / 3)

