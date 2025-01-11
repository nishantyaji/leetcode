# Problem 1400
import collections


class ConstructKPalindromeString:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        cntr = collections.Counter(s)
        odds = [1 for k, v in cntr.items() if v % 2 == 1]
        return False if len(odds) > k else True


if __name__ == '__main__':
    c = ConstructKPalindromeString()
    print(c.canConstruct("annabelle", 2))  # True
    print(c.canConstruct("leetcode", 3))  # False
    print(c.canConstruct("true", 4))  # True
