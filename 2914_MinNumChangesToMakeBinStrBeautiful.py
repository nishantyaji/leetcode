# Problem 2914


class MinNumChangesToMakeBinStrBeautiful:
    def minChanges(self, s: str) -> int:
        return sum([int(x) ^ int(y) for x, y in zip(s[::2], s[1::2])])
        # return sum([1 for i in range(0, len(s), 2) if s[i] != s[i + 1]])