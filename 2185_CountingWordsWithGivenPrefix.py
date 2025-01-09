# Problem 2185
from typing import List


class CountingWordsWithGivenPrefix:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return sum([1 for s in words if s.startswith(pref)])
