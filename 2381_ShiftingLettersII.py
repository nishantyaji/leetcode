# Problem 2381
import collections
from typing import List


class ShiftingLettersII:
    class Solution:
        def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
            dp = collections.defaultdict(int)
            for start, end, dire in shifts:
                if dire:
                    dp[start] += 1
                    dp[end + 1] -= 1
                else:
                    dp[start] -= 1
                    dp[end + 1] += 1

            cum, res = 0, []
            for i in range(len(s)):
                cum += dp[i]
                temp = (ord(s[i]) + (cum % 26))
                if temp > ord('z'):
                    temp = temp - ord('z') + ord('a') - 1
                res += [str(chr(temp))]
            return "".join(res)
