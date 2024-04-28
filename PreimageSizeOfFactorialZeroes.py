#Problem 793
import math
class PreimageSizeOfFactorialZeroes:
    def preimageSizeFZF(self, k: int) -> int:
        if k == 0:
            return 5

        approx = 4 * k
        for i in range(approx, approx*2):
            if self.trailingZeroes(i) == k:
                return 5
            if self.trailingZeroes(i) > k:
                return 0
        return 0

    def trailingZeroes(self, n: int) -> int:
        if n < 5:
            return 0
        pow_highest = int(math.log(n, 5))
        result = 0

        for pow_highest in range(pow_highest, 0, -1):
            base = int(math.pow(5, pow_highest))
            result += int(n / base)
        return result


if __name__ == '__main__':
    p = PreimageSizeOfFactorialZeroes()
    print(p.preimageSizeFZF(38995104))
    print(p.preimageSizeFZF(50211))
    print(p.preimageSizeFZF(71))