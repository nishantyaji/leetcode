# Problem 2787
import functools
import math


class WaysToExpressIntAsSumOfPowers:

    def numberOfWays(self, n: int, x: int) -> int:
        max_limit = math.ceil(pow(n, 1/x))
        return self.fun_dp(n, x, max_limit)

    @functools.cache
    def fun_dp(self, num: int, x: int, max_limit: int):
        if num == 0:
            return 1
        else:
            if max_limit == 1:
                return 1 if num == 1 else 0
        temp = pow(max_limit, x)
        if temp > num:
            return self.fun_dp(num, x, max_limit - 1)
        return (self.fun_dp(num, x, max_limit - 1) + self.fun_dp(num - temp, x, max_limit - 1)) % 1000000007


if __name__ == '__main__':
    w = WaysToExpressIntAsSumOfPowers()
    print(w.numberOfWays(64, 3))  # 1
    print(w.numberOfWays(8, 1))  # 6
    print(w.numberOfWays(10, 2))  # 1
    print(w.numberOfWays(4, 1))  # 2
