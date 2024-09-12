# Problem 1684
from typing import List


class CountNumOfConsistentStrings:

    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        supr = set(list(allowed))
        return sum([1 for x in words if self.is_subset(set(list(x)), supr)])

    def is_subset(self, sub: set, supr: set):
        return len(sub - supr) == 0
