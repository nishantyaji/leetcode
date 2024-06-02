# Problem 3110

class ScoreOfAString:
    def scoreOfString(self, s: str) -> int:
        return sum([abs(ord(s[i + 1]) - ord(s[i])) for i in range(0, len(s) - 1)])
