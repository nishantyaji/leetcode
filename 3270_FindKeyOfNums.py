# Problem 3270

class FindKeyOfNums:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:

        def pad_(s: str):
            rem = 4 - len(s)
            if rem > 0:
                return "".join((["0"] * rem)) + s
            return s

        str1, str2, str3 = pad_(str(num1)), pad_(str(num2)), pad_(str(num3))

        res = 0
        for i in range(4):
            val = min(ord(str1[i]) - ord('0'), ord(str2[i]) - ord('0'), ord(str3[i]) - ord('0'))
            res = 10 * res + val
        return res


if __name__ == '__main__':
    b = BiweeklyContest138P1()
    print(b.generateKey(1, 10, 1000))
    print(b.generateKey(987, 879, 798))
    print(b.generateKey(1, 2, 3))