# Problem 2011
from typing import List


class FinalValueOfVariableAfterPerformingOps:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        mp = {"--X": lambda x: x - 1, "X--": lambda x: x - 1, "++X": lambda x: x + 1, "X++": lambda x: x + 1}
        y = 0
        for op in operations:
            y = mp[op](y)
        return y
