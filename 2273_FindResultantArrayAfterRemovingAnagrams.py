# Problem 2273
import collections
from typing import List


class FindResultantArrayAfterRemovingAnagrams:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        def is_anagram(w1: str, w2: str):
            cntr1 = collections.Counter(list(w1))
            cntr2 = collections.Counter(list(w2))
            return cntr1 == cntr2

        stack = []
        for w in words:
            if stack and is_anagram(stack[-1], w):
                continue
            else:
                stack.append(w)
        return stack
