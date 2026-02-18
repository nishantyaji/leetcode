# Problem 190

class ReverseBits:
    def reverseBits(self, n: int) -> int:
        return int(format(n, "b").rjust(32, "0")[::-1], 2)