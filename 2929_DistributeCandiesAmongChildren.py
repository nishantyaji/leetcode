# Problem 2929


class DistributeCandiesAmongChildren:

    def distributeCandies(self, n: int, limit: int) -> int:

        def split2(numm: int, lim: int):
            if numm < 0:
                return -1
            if numm < lim:
                return numm + 1
            if numm > 2 * lim:
                return -1
            elif numm == 2 * lim:
                return 1
            else:
                return lim - (numm - lim) + 1

        res = 0
        for i in range(0, limit + 1):
            temp = split2(n - i, limit)
            if temp > 0:
                res += temp
        return res
