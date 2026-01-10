# Problem 712
import functools


class MinASCIIDeleteSumForTwoStrings:
    @functools.cache
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        if not s1:
            return self.value(s2)
        if not s2:
            return self.value(s1)
        if s1[0] == s2[0]:
            return self.minimumDeleteSum(s1[1:], s2[1:])
        l1 = ord(s1[0]) + self.minimumDeleteSum(s1[1:], s2)
        l2 = ord(s2[0]) + self.minimumDeleteSum(s1, s2[1:])
        return min(l1, l2)

    @functools.cache
    def value(self, s: str):
        res = 0
        for c in s:
            res += ord(c)
        return res
