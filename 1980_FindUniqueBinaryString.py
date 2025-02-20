# Problem 1980
from typing import List


class FindUniqueBinaryString:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        l = len(nums[0])
        s = set(nums)
        for i in range(0, l + 1):
            t = format(i, "b").rjust(l, "0")
            if t not in s:
                return t
        return ""
