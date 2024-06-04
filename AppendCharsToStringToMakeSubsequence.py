# Problem 2486

class AppendCharsToStringToMakeSubsequence:
    def appendCharacters(self, s: str, t: str) -> int:
        right = 0
        for idx, ch in enumerate(s):
            if ch == t[right]:
                right += 1
        return len(t) - right
