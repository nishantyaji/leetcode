# Problem 2264

class Largest3SameDigitNumInStr:
    def largestGoodInteger(self, num: str) -> str:

        num_str = str(num)
        prev, count = "a", 1
        flags = [False] * 10
        for n in num_str:
            if n == prev:
                count += 1
                if count == 3:
                    flags[int(n)] = True
            else:
                count = 1
            prev = n

        for i in range(9, -1, -1):
            if flags[i] == True:
                return "".join([str(i)] * 3)
        return ""
