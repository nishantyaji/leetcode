# Problem 2109
from typing import List


class AddingSpacesToString:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        spaces = [0] + spaces + [len(s)]
        spaces.sort()
        tokens = [s[spaces[i]:spaces[i + 1]] for i in range(len(spaces) - 1)]
        return " ".join(tokens)
