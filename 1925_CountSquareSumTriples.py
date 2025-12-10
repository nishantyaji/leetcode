# Problem 1925

class CountSquareSumTriples:
    def countTriples(self, n: int) -> int:
        res = 0
        for a in range(1, n):
            for b in range(1, n):
                for c in range(max(a, b) + 1, n + 1):
                    if a * a + b * b == c * c:
                        res += 1
        return res