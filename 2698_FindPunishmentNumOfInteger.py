# Problem 2698
import functools


class FindPunishmentNumOfInteger:

    def punishmentNumber(self, n: int) -> int:

        @functools.cache
        def recurse(s: str, numm: int, run_sum: int):
            if not s:
                if run_sum == numm:
                    return True
                return False
            else:
                if run_sum > numm:
                    return False

            s_int = int(s)
            if s_int + run_sum == numm:
                return True
            for i in range(1, len(s)):
                pre, post = s[:i], s[i:]
                if recurse(post, numm, run_sum + int(pre)):
                    return True
            return False

        def partitionable(numm: int):
            squ = numm * numm
            return recurse(str(squ), numm, 0)

        res = 0
        for i in range(1, n + 1):
            if partitionable(i):
                res += (i * i)
        return res


if __name__ == '__main__':
    f = FindPunishmentNumOfInteger()
    print(f.punishmentNumber(10))
    print(f.punishmentNumber(37))
