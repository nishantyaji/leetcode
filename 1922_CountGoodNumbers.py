# Problem 1922
import math


class CountGoodNumbers:
    def countGoodNumbers(self, n: int) -> int:
        if n == 1:
            return 5
        mod_base = 1000000007
        num_even, num_odd = math.ceil(n /2), math.floor(n/2)
        ans = (5 * pow(5, num_even - 1, mod_base) * pow(4, num_odd, mod_base)) % mod_base
        return ans