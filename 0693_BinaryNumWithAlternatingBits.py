# Problem 693

class BinaryNumWthAlternatingBits:

    def hasAlternatingBits(self, n: int) -> bool:
        b, prev = format(n, "b"), "~"
        for c in b:
            if c == prev:
                return False
            prev = c
        return True