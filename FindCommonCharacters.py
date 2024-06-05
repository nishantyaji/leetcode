# Problem 1002

import math
from typing import List


class FindCommonCharacters:
    def commonChars(self, words: List[str]) -> List[str]:
        result = [math.inf] * 26
        for word in words:
            this_result = [0] * 26
            for ch in word:
                this_result[ord(ch) - ord('a')] += 1
            for i in range(26):
                result[i] = min(result[i], this_result[i])

        return_list = []
        for idx, count in enumerate(result):
            for _ in range(count):
                return_list.append(chr(idx + ord('a')))

        return return_list