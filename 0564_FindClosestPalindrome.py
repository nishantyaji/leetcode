# Problem 564

import math
import sys


class FindClosestPalindrome:
    def nearestPalindromic(self, n: str) -> str:
        num = int(n)
        if num == 0:
            return "1"
        elif num <= 10:
            return str(num - 1)
        elif num == 11:
            return "9"

        if self.is_pow_of_10(num):
            return str(num - 1)

        is_odd = len(n) % 2 == 1
        prefix = n[:(len(n) + 1) // 2]

        rem_dig = len(n) - len(prefix)
        pr_int = int(prefix)
        temps = [(pr_int + 1) * (10 ** rem_dig), pr_int * (10 ** rem_dig), (pr_int - 1) * (10 ** rem_dig)]
        min_diff = sys.maxsize

        res = -1
        for temp in temps:
            pal = self.extend_(temp, is_odd)
            diff = abs(pal - num)
            if diff != 0 and diff <= min_diff:
                min_diff = diff
                res = pal

        return str(res)

    def extend_(self, num: int, is_odd: bool) -> int:
        s = str(num)
        rev = int(s[:len(s) // 2][::-1]) if is_odd else int(s[::-1])
        return num + rev

    def is_pow_of_10(self, num: int):
        pw = int(math.log10(num))
        res = 10 ** pw
        return res == num


if __name__ == '__main__':
    f = FindClosestPalindrome()
    print(f.nearestPalindromic("1000"))
    print(f.nearestPalindromic("230"))
    print(f.nearestPalindromic("123"))
    print(f.nearestPalindromic("1"))
