# Problem 233
import functools
import math


class NumberOfDigitOne:

    @functools.cache
    def countDigitOne(self, n: int) -> int:
        if n < 10:
            return 0 if n == 0 else 1
        num_digits = int(math.log10(n))
        base = int(math.pow(10, num_digits))
        q, r = int(n / base), n % base
        result = 0
        if q == 1:
            result += (r + 1) + self.countDigitOne(base - 1)
        else:
            result += base + self.countDigitOne(base - 1) * q
        result += self.countDigitOne(r)
        return result


if __name__ == '__main__':
    n = NumberOfDigitOne()
    print(n.countDigitOne(20))
    print(n.countDigitOne(13))
