class FindKthBitInNthBinString:
    def findKthBit(self, n: int, k: int) -> str:
        def inv(c: str):
            return "1" if c == "0" else "0"

        if n == 1:
            return "0"
        if k == 2 ** (n - 1):
            return "1"
        if k > 2 ** (n - 1):
            return inv(self.findKthBit(n - 1, (2 ** n) - k))
        return self.findKthBit(n - 1, k)


if __name__ == '__main__':
    f = FindKthBitInNthBinString()
    print(f.findKthBit(3, 5)) # 0
    print(f.findKthBit(4, 11)) # 1
    print(f.findKthBit(3, 5))
