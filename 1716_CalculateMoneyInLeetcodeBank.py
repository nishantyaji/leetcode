# Problem 1716

class CalculateMoneyInLeetcodeBank:
    def totalMoney(self, n: int) -> int:
        q, r = divmod(n, 7)

        res = 28 * q + (q - 1) * q * 7 // 2 + r * (r + 1) // 2 + r * q
        return res
