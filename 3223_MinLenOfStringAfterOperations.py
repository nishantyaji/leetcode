# Problem 3223
import collections


class MinLenOfStringAfterOperations:

    def minimumLength(self, s: str) -> int:
        cntr = collections.Counter(s)
        res = 0
        for k, v in cntr.items():
            if v % 2 == 0:
                if v > 0:
                    res += 2
            else:
                res += 1
        return res


if __name__ == '__main__':
    m = MinLenOfStringAfterOperations()
    print(m.minimumLength("abaacbcbb"))
