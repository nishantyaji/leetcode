# Problem 3541
import collections


class FindMostFrequentVowelAndConsonant:
    def maxFreqSum(self, s: str) -> int:
        # this code can be compressed and code golfed
        mp_v = collections.Counter()
        mp_c = collections.Counter()
        mp_v["a"] = 0
        mp_c["z"] = 0
        vowels = {"a", "e", "i", "o", "u"}
        for c in s:
            if c in vowels:
                mp_v[c] += 1
            else:
                mp_c[c] += 1

        return max(mp_v.values()) + max(mp_c.values())
