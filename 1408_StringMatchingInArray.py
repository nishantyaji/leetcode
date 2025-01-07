# Problem 1408
from typing import List


class StringMatchingInArray:

    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key=lambda x: len(x))
        res_set = set()
        for i in range(len(words)):
            for j in range(i):
                if words[i].find(words[j]) > -1:
                    res_set.add(words[j])
        return list(res_set)
