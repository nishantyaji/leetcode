# Problem 1790
import collections


class CheckIfOneStringSwapCanMakeStringsEqual:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        cntr1 = collections.Counter(s1)
        cntr2 = collections.Counter(s2)
        if cntr1 != cntr2:
            return False

        cnt = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                cnt += 1
            if cnt > 2:
                return False

        return True
