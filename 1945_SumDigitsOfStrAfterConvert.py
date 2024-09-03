# Problem 1945

class SumDigitsOfStrAfterConvert:
    def getLucky(self, s: str, k: int) -> int:
        vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8]
        nums = list(map(lambda x: vals[x], map(lambda y: ord(y) - ord('a'), list(s))))
        res = 0
        for _ in range(k):
            res = sum(nums)
            nums = list(map(int, list(str(res))))
        return res

if __name__ == '__main__':
    s = SumDigitsOfStrAfterConvert()
    print(s.getLucky("iiii", 1))
    print(s.getLucky("leetcode", 2))
    print(s.getLucky("zbax", 2))
