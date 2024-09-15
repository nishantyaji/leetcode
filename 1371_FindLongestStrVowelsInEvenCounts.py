# Problem 1371
import collections


class FindLongestStrVowelsInEvenCounts:
    def findTheLongestSubstring(self, s: str) -> int:
        grps = collections.defaultdict(list)
        grps[0].append(-1)
        vowels = {"a", "e", "i", "o", "u"}
        cntr = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

        def add_ch(char: str) -> int:
            if char in vowels:
                cntr[char] = (cntr[char] + 1) % 2
            return cntr["u"] + 2 * cntr["o"] + 4 * cntr["i"] + 8 * cntr["e"] + 16 * cntr["a"]

        for i, char in enumerate(s):
            grps[add_ch(char)].append(i)

        return max([v[-1] - v[0] for k, v in grps.items()])

if __name__ == '__main__':
    f = FindLongestStrVowelsInEvenCounts()
    print(f.findTheLongestSubstring("eleetminicoworoep"))
    print(f.findTheLongestSubstring("leetcodeisgreat"))
    print(f.findTheLongestSubstring("bcbcbc"))