# Problem 916
import collections
from typing import Dict, List


class WordSubsets:

    def wordSubsetsFaster(self, words1: List[str], words2: List[str]) -> List[str]:
        u_map = {}
        for w in words2:
            cntr = collections.Counter(w)
            for k, v in cntr.items():
                u_map[k] = max(u_map[k], v) if k in u_map else v

        res = []
        for w in words1:
            cntr = collections.Counter(w)
            skip = False
            for k, v in u_map.items():
                if k not in cntr or cntr[k] < v:
                    skip = True
                    break
            if not skip:
                res.append(w)
        return res


def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
    result = []
    subDict = self.mergeDict(words2)
    for super in words1:
        superDict = self.convertToDict(super)
        if self.isDictSubset(superDict, subDict):
            result.append(super)
    return result


def mergeDict(self, words: List[str]) -> Dict[str, int]:
    mergeResult = {}
    for word in words:
        result = self.convertToDict(word)
        for ch in result.keys():
            if ch not in mergeResult.keys() or mergeResult[ch] < result[ch]:
                mergeResult[ch] = result[ch]

    return mergeResult


def convertToDict(self, word: str) -> Dict[str, int]:
    result = {}
    for ch in word:
        if ch in result:
            count = result[ch]
            result[ch] = count + 1
        else:
            result[ch] = 1
    return result


def isDictSubset(self, super: Dict[str, int], sub: Dict[str, int]) -> bool:
    for ch in sub.keys():
        if ch not in super.keys():
            return False
        else:
            subCount = sub[ch]
            superCount = super[ch]
            if subCount > superCount:
                return False
    return True


if __name__ == '__main__':
    w = WordSubsets()
    print(w.wordSubsets(["amazon", "apple", "facebook",
                         "google", "leetcode"], ["e", "o"]))
    print(w.wordSubsets(["amazon", "apple", "facebook",
                         "google", "leetcode"], ["e", "l"]))
    print(w.wordSubsets(["amazon", "apple", "facebook",
                         "google", "leetcode"], ["lo", "eo"]))
    print(w.wordSubsets(["amazon", "apple", "facebook",
                         "google", "leetcode"], ["e", "oo"]))
