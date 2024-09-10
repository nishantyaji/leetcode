# Problem 3271

class HashDividedString:
    def stringHash(self, s: str, k: int) -> str:
        res = ""
        run = 0
        for i, c in enumerate(s):
            run += ord(c) - ord('a')
            if i % k == k - 1:
                temp = str(chr(ord('a') + (run % 26)))
                res += temp
                run = 0
        return res


if __name__ == '__main__':
    b = HashDividedString()
    print(b.stringHash("abcd", 2))
    print(b.stringHash("mxz", 3))
    print(b.stringHash("mxz", 1))
