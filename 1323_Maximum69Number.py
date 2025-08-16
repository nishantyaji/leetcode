# Problem 1323
import math


class Maximum69Number:
    def maximum69Number(self, num: int) -> int:
        resultStr = ""
        found = False
        for character in str(num):
            if found == False and character == "6":
                first = "9"
                found = True
            else:
                first = character
            resultStr = resultStr + first
        return int(resultStr)

    def maximum69Number_fast(self, num: int) -> int:
        digits = math.floor(math.log10(num)) + 1
        for i in range(digits - 1, -1, -1):
            q, r = divmod(num, pow(10, i))
            if q % 10 == 6:
                return num + pow(10, i) * 3
        return num


if __name__ == '__main__':
    m = Maximum69Number()
    print(m.maximum69Number(9669))
