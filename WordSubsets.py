# Problem 916
from calendar import c
from typing import Dict, List


class WordSubsets:

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
                print(ch, ':', result[ch])
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
