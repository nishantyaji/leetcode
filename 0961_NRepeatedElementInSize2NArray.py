# Problem 961
from typing import List


class NRepeatedElementInSize2NArray:
    def repeatedNTimes(self, nums: List[int]) -> int:
        s = set()
        for n in nums:
            if n in s:
                return n
            s.add(n)
        return 0

