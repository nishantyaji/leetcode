# Problem 3227
import collections


class VowelsGameInAString:
    def doesAliceWin(self, s: str) -> bool:
        # this code can be compressed and code-golfed
        cntr = collections.Counter(list(s))
        vowels = ["a", "e", "i", "o", "u"]
        vowel_count = 0
        for v in vowels:
            vowel_count += cntr[v]
        if vowel_count == 0:
            return False
        else:
            return True
