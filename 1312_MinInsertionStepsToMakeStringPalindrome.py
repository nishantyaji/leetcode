# Problem 1312
import sys


class MinInsertionStepsToMakeStringPalindrome:

    def distance(self, w1: str, w2: str):
        if not w1:
            return len(w2)
        if not w2:
            return len(w1)
        if w1[0] == w2[0]:
            return self.distance(w1[1:], w2[1:])
        else:
            d1 = 1 + self.distance(w1[1:], w2)
            d2 = 1 + self.distance(w1, w2[1:])
            return min(d1, d2)

    def minInsertions(self, s: str) -> int:
        res = sys.maxsize
        for i in range(len(s)):
            rev = s[:i][::-1]
            d1 = self.distance(rev, s[i:])
            d2 = self.distance(rev, s[i + 1:])
            res = min(min(d1, res), d2)
        return res


if __name__ == '__main__':
    m = MinInsertionStepsToMakeStringPalindrome()
    print(m.minInsertions("zzazz"))
    print(m.minInsertions("mbadm"))
    print(m.minInsertions("leetcode"))
