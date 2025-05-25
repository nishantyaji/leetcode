# Problem 2131
import collections
from typing import List


class LongestPalindromeByConcatenating2LetterWords:

    def longestPalindrome(self, words: List[str]) -> int:
        self_reflexive = 0
        cntr = collections.Counter(words)
        full_len = 0
        for x in cntr.keys():
            if x == x[::-1]:
                if cntr[x] % 2 == 1:
                    self_reflexive = 1
                full_len += (4 * (cntr[x] // 2))
            else:
                full_len += (2 * min(cntr[x], cntr[x[::-1]]))
        return full_len + self_reflexive * 2

