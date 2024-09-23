import bisect
import itertools
import math
import operator


class KthSmallestInLexicographicalOrder:

    def findKthNumber(self, n: int, k: int) -> int:
        if k == 1:
            return 1
        return self.recurse_strict(n, k, 0, True)

    def recurse_strict(self, num: int, k: int, prefix: int, is_init: bool):
        if num == 0 or k == 0:
            return prefix
        num_digits = int(math.log(num, 10)) + 1
        msd = num // 10 ** (num_digits - 1)

        pre_sum = 0
        for i in range(0, num_digits-1):
            pre_sum += (10 ** i)

        steps = [pre_sum] * (9 if is_init else 10)
        msd_new = msd-1 if is_init else msd
        for i in range(0, msd_new):
            steps[i] += (10 ** (num_digits-1))

        steps[msd_new] += (num % (10 ** (num_digits - 1))) if num_digits > 1 else 1
        acc_steps = list(itertools.accumulate(steps, operator.add, initial=0 if is_init else 1))
        idx = bisect.bisect_left(acc_steps, k)
        if acc_steps[idx+1] == k:
            if idx == 1:
                return prefix
            else:
                return 10 * prefix + idx - 2
        else:
            prefix = 10 * prefix + idx

        return self.recurse_strict(num - msd * (10 ** (num_digits - 1)), k - acc_steps[idx-1], prefix, False)


if __name__ == '__main__':
    k = KthSmallestInLexicographicalOrder()
    print(k.findKthNumber(2, 2))
    print(k.findKthNumber(13, 2))
    print(k.findKthNumber(1, 1))

