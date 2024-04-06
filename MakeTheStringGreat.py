#Problem 1544

class MakeTheStringGreat:
    def makeGood(self, s: str) -> str:
        present_len = len(s)
        while True:
            s = self.recurse(s)
            if len(s) == present_len:
                return s
            else:
                present_len = len(s)

    def recurse(self, s: str) -> str:
        for i in range(0, len(s) - 1):
            diff = ord(s[i]) - ord(s[i + 1])
            if diff == 32 or diff == -32:
                return s[:i] + s[i + 2:]
        return s

