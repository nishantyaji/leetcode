# Problem 2559
import itertools
from typing import List


class CountVowelsStringsInRanges:

    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {"a", "e", "i", "o", "u"}
        arr = [1 if w[0] in vowels and w[-1] in vowels else 0 for w in words]
        prefix = [0] + list(itertools.accumulate(arr))
        return [prefix[r + 1] - prefix[l] for l, r in queries]

