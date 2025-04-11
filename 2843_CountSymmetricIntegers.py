# Problem 2843
import bisect


class CountSymmetricIntegers:

    def countSymmetricIntegers(self, low: int, high: int) -> int:

        res = 0
        for i in range(max(low, 11), min(high + 1, 100)):
            if i // 10 == i % 10:
                res += 1

        def dig2sum(numm: int):
            return numm // 10 + numm % 10

        for x in range(max(low, 1000), min(high + 1, 10000)):
            if dig2sum(x // 100) == dig2sum(x % 100):
                res += 1

        return res

    def countSymmetricIntegers_slow(self, low: int, high: int) -> int:
        arr = [11 * i for i in range(1, 10)]

        def dig2sum(numm: int):
            return numm // 10 + numm % 10

        for i in range(1000, 10000):
            if dig2sum(i // 100) == dig2sum(i % 100):
                arr.append(i)

        lidx = bisect.bisect_left(arr, low)
        ridx = bisect.bisect_right(arr, high)
        return ridx - lidx


if __name__ == '__main__':
    c = CountSymmetricIntegers()
    print(c.countSymmetricIntegers(1200, 1230))
