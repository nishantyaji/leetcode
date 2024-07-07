# Problem 3210

class FindTheEncryptedString:
    def getEncryptedString(self, s: str, k: int) -> str:
        return ''.join([s[(i + k) % len(s)] for i, c in enumerate(s)])
