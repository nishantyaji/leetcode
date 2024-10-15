# Problem 2938

class SeparateBlackAndWhiteBalls:

    def minimumSteps(self, s: str) -> int:
        zeroes = sum([1 for c in s if c == "0"])
        ones_out, zeroes_out = [], []
        for i, c in enumerate(s):
            if c == "1" and i <= zeroes - 1:
                ones_out.append(i)
            elif c == "0" and i >= zeroes:
                zeroes_out.append(i)
        return sum([abs(x - zeroes_out[i]) for i, x in enumerate(ones_out)])


if __name__ == '__main__':
    s = SeparateBlackAndWhiteBalls()
    print(s.minimumSteps("101"))
    print(s.minimumSteps("100"))
    print(s.minimumSteps("0111"))
