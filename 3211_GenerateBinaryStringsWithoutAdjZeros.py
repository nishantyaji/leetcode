# Problem 3211
from typing import List


class GenerateBinaryStringsWithoutAdjZeros:
    def validStrings(self, n: int) -> List[str]:
        result = []
        self.recurse('0', n, result)
        self.recurse('1', n, result)
        return result

    def recurse(self, running: str, n: int, result: List[str]):
        if len(running) == n:
            result.append(running)
            return
        if running[-1] == '1':
            self.recurse(running + '0', n, result)
        self.recurse(running + '1', n, result)
