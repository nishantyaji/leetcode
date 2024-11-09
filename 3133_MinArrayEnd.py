# Problem 3133

class MinArrayEnd:
    def minEnd(self, n: int, x: int) -> int:
        nstr = list(format(n - 1, "b"))
        xstr = list(format(x, "b"))[::-1]
        joined = "".join(reversed([nstr.pop() if c == "0" and nstr else c for c in xstr]))
        return int("".join(nstr) + joined, 2)


if __name__ == '__main__':
    m = MinArrayEnd()
    print(m.minEnd(3, 4))
    print(m.minEnd(2, 7))
