# Problem 2999
import functools
import math


class CountNumOfPowerfulIntegers:

        @functools.cache
        def recurse(self, num: int, limit: int):
            if num <= 9:
                return min(num, limit) + 1
            digits = math.floor(math.log10(num)) + 1
            msd, remain = divmod(num, (pow(10, digits - 1)))
            if msd > limit:
                return (limit + 1) * pow(limit + 1, digits - 1)
            else:
                res = msd * pow(limit + 1, digits - 1)

            if msd <= limit:
                # remain == 0 is important since there is just 1 number with the latest prefix
                res += (self.recurse(remain, limit) if remain > 0 else 1)
            return res

        def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:

            suf, suf_digits = int(s), len(s)
            suf_base = pow(10, suf_digits)

            if suf > finish:
                return 0
            elif suf == finish:
                return 1

            fq, fr = divmod(finish, suf_base)
            if fr < suf:
                fq -= 1

            sq, sr = divmod(start, suf_base)
            if sr > suf:
                sq += 1

            hi = self.recurse(fq, limit)
            lo = self.recurse(sq - 1, limit)
            return hi - lo