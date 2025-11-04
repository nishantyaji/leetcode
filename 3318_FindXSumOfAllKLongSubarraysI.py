# Problem 3318
import collections
from typing import List


class FindXSumOfAllKLongSubarraysI:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        cntr = collections.Counter(nums[:k])

        def xtop(cn):
            pairs = [(v, k) for k, v in cn.items()]
            pairs.sort(key=lambda y: -51 * y[0] - y[1])
            temp = [z[0] * z[1] for z in pairs]
            return sum(temp[:x])

        res = [xtop(cntr)]
        for i in range(k, len(nums)):
            cntr[nums[i - k]] -= 1
            if cntr[nums[i - k]] == 0:
                del cntr[nums[i - k]]
            cntr[nums[i]] += 1
            res.append(xtop(cntr))
        return res
