# Problem 1930
import copy


class UniqueLen3PalindromicSubsequences:
    def countPalindromicSubsequence(self, s: str) -> int:
        temp, suffix, res = set(), [], set()
        for i in range(len(s) - 1, -1, -1):
            if s[i] not in temp:
                temp.add(s[i])
            suffix.append(copy.deepcopy(temp))
        suffix.reverse()
        temp = set()
        for i in range(len(s) - 1):
            if i > 0:
                ixn = temp.intersection(suffix[i + 1])
                res.update([x + s[i] for x in ixn])
            if s[i] not in temp:
                temp.add(s[i])
        return len(res)
