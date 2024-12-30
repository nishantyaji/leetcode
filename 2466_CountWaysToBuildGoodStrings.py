# Problem 2466
import math


class CountWaysToBuildGoodStrings:

    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        # faster. DP
        mn, mx, base = min(zero, one), max(zero, one), 1000000007
        dp = [0] * (high + mx + 1)
        dp[mn] += 1
        dp[mx] += 1
        for i in range(mn, high + 1):
            if dp[i]:
                dp[i + zero] = (dp[i + zero] + dp[i]) % base
                dp[i + one] = (dp[i + one] + dp[i]) % base
        return sum(dp[low: high + 1]) % base

    def countGoodStrings2(self, low: int, high: int, zero: int, one: int) -> int:
        # apparently slow
        ones_high, base = math.floor(low / one), 1000000007
        res = 0
        for i in range(0, ones_high + 1):
            zeroes_low = math.ceil((low - i * one) / zero)
            zeroes_high = math.floor((high - i * one) / zero)
            for j in range(zeroes_low, zeroes_high + 1):
                res = (res + math.comb(i + j, j)) % base
        return res


if __name__ == '__main__':
    c = CountWaysToBuildGoodStrings()
    print(c.countGoodStrings(2, 3, 1, 2))  # 5
    print(c.countGoodStrings(3, 3, 1, 1))  # 8
