# Problem 1415

class TheKthLexicographicalStringOfAllHappyStringsOfLengthN:
    def getHappyString(self, n: int, k: int) -> str:
        k -= 1
        base = pow(2, n - 1)
        if k >= 3 * base:
            return ""
        quot, remain = divmod(k, base)
        res = ""
        if quot == 0:
            res += "a"
        elif quot == 1:
            res += "b"
        else:
            res += "c"
        mp = {"a": {0: "b", 1: "c"}, "b": {0: "a", 1: "c"}, "c": {0: "a", 1: "b"}}

        def recur(level: int, prev: str, rem: int):
            if level > 0:
                q, r = divmod(rem, pow(2, level - 1))
                return mp[prev][q] + recur(level - 1, mp[prev][q], r)
            return ""

        return res + recur(n - 1, res[0], remain)

if __name__ == '__main__':
    t = TheKthLexicographicalStringOfAllHappyStringsOfLengthN()
    print(t.getHappyString(3, 9))
    print(t.getHappyString(10, 100))
