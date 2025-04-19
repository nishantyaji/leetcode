# Problem 1611
import math


class MinOneBitOpsToMakeIntegersZero:
    def reduce_(self, n: int):
        if n <= 1:
            return n
        x = 1 + math.floor(math.log2(n))
        half = pow(2, x - 1)
        xor_val = 0 if x % 2 == 0 else 1
        return xor_val ^ self.reduce_(half - 1 - (n - half))

    def minimumOneBitOperations(self, n: int) -> int:
        if n <= 1:
            return n

        pw = math.floor(math.log2(n))
        res = pow(2, pw)
        pw -= 1
        while pw >= 0:
            q, r = divmod(n, pow(2, pw))
            dig = self.reduce_(q)
            res = (res | (dig * pow(2, pw)))
            pw -= 1

        return res
