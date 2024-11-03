# Problem 592
import math


class FractionAddSubtract:
    def fractionAddition(self, expression: str) -> str:

        res = Fraction(0, 1)
        mul, start = 1, 0
        if expression[0] == "-":
            mul = -1
            start = 1
        token = ""
        for i, c in enumerate(expression[start:]):
            if c == "-":
                res = res.op_(Fraction.init_str(token), mul)
                mul = -1
                token = ""
            elif c == "+":
                res = res.op_(Fraction.init_str(token), mul)
                mul = 1
                token = ""
            else:
                token += c
        res = res.op_(Fraction.init_str(token), mul)

        return str(res.num) + "/" + str(res.den)


class Fraction:
    def init_str(s: str):
        [ns, ds] = s.split("/")
        return Fraction(int(ns), int(ds))

    def __init__(self, n: int, d: int):
        self.num = n
        self.den = d

    def op_(self, f: 'Fraction', mul: int):
        n = f.den * self.num + mul * self.den * f.num
        d = self.den * f.den
        g = math.gcd(n, d)
        return Fraction(n // g, d // g)


if __name__ == '__main__':
    f = FractionAddSubtract()
    print(f.fractionAddition("-1/2+1/2"))
    print(f.fractionAddition("-1/2+1/2+1/3"))
    print(f.fractionAddition("1/3-1/2"))
