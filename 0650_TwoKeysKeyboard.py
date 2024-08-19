# Problem 650
import math


class TwoKeysKeyboard:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0

        temp = [0] * 1000
        temp[0] = 1
        for i in range(2, int(math.sqrt(1000)) + 1):
            for j in range(2, 1 + (1000 // i)):
                temp[(i * j) - 1] = 1
        primes = [i + 1 for i, x in enumerate(temp) if x == 0]
        primeset = set(primes)

        if n in primeset:
            return n

        def power(x: int, base: int):
            if x % base > 0:
                return [x, 0]

            pw = 0
            while x % base == 0:
                x = x // base
                pw += 1
            return [x, pw]

        lim, res = int(math.sqrt(n)), 0
        for p in primes:
            if n == 1:
                break
            if n % p == 0:
                [n, x] = power(n, p)
                res += (p * x)
                if n in primeset and n > lim:
                    res += n
                    n = 1
        return res


if __name__ == '__main__':
    t = TwoKeysKeyboard()
    print(t.minSteps(6))
    print(t.minSteps(189))
    print(t.minSteps(3))
    print(t.minSteps(1))
