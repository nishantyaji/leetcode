# Problem 2900
from typing import List


class LongestUneqAdjGroupsSubsequenceI:

    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        res, run = [], None
        for i in range(len(words)):
            if run != groups[i]:
                run = groups[i]
                res.append(words[i])
        return res
