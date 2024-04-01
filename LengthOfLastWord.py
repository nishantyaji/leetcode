#Problem 58

class LengthOfLastWord:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])