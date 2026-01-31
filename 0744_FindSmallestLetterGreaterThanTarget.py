# Problem 744
from bisect import bisect
from typing import List


class FindSmallestLetterGreaterThanTarget:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        return letters[(bisect.bisect_right(letters, target)) % len(letters)]
