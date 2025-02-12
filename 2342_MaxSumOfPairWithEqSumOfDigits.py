# Problem 2342
from typing import List


class MaxSumOfPairWithEqSumOfDigits:

    def maximumSum(self, nums: List[int]) -> int:
        mp = {}

        def ret_pair(key, new):
            if key not in mp:
                mp[key] = [new]
                return -1
            elif len(mp[key]) == 1:
                temp = mp[key][0]
                mp[key] = [temp, new] if temp > new else [new, temp]
            else:
                largest, larger = mp[key]
                if new > largest:
                    mp[key] = [new, largest]
                elif largest >= new > larger:
                    mp[key] = [largest, new]
            return sum(mp[key])

        def sum_digits(numm):
            return sum(map(int, str(numm)))

        res = -1
        for n in nums:
            temp = ret_pair(sum_digits(n), n)
            res = max(res, temp)
        return res
