# Problem 30
import bisect
import collections
import copy
from typing import List


class SubStrWithConcatAllWords:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # There is a more efficient way where in we maintain map with
        # the find/indices of the different words.
        # and then in the window of length: len(words[0]) * len(words)
        # we check if all words are in place
        # Corner case when words are not unique

        words.sort()
        res = []
        if len(words[0]) == 1 and words[0] == words[-1]:
            des = "".join([words[0]] * len(words))
            for i in range(0, len(s) - len(words) + 1):
                if s[i:i + len(words)] == des:
                    res.append(i)
            return res

        obj, cnt = collections.defaultdict(int), collections.defaultdict(int)
        for w in words:
            for x in w:
                obj[x] += 1
        win_len = sum([len(x) for x in words])

        if len(s) < win_len:
            return []
        for i in range(win_len - 1):
            cnt[s[i]] += 1

        for i in range(win_len - 1, len(s)):
            cnt[s[i]] += 1
            if i > win_len - 1:
                self.sub_(cnt, s[i - win_len])

            if self.is_eq(cnt, obj):
                if self.check(s[i - win_len + 1:i + 1], words):
                    res.append(i - win_len + 1)
        return res

    def check(self, s: str, words: List[str]):
        words2 = copy.deepcopy(words)
        for j in range(0, len(words)):
            start, end = j * len(words[0]), (j + 1) * len(words[0])
            index = bisect.bisect_left(words2, s[start:end])
            if index < len(words2) and words2[index] == s[start:end]:
                words2.pop(index)
            else:
                return False
        return True

    def is_eq(self, d1: dict, d2: dict):
        if len(d1) != len(d2):
            return False
        for k, v in d1.items():
            # Do not directly call d2[k] != v comparison
            # because d2 is a defaultdict
            # therefore creates d2[k] as 0 if k is not present
            # during comparison
            if k not in d2 or d2[k] != v:
                return False
        return True

    def sub_(self, d1: dict, key: str):
        if key in d1:
            d1[key] -= 1
            if d1[key] == 0:
                del d1[key]


if __name__ == '__main__':
    s = SubStrWithConcatAllWords()
    print(s.findSubstring("a", ["a"]))
    # [0]
    print(s.findSubstring("barfoothefoobarman", ["foo", "bar"]))
    # [0, 9]
    print(s.findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "word"]))
    # []
    print(s.findSubstring("barfoofoobarthefoobarman", ["bar", "foo", "the"]))
    # [6, 9, 12]
