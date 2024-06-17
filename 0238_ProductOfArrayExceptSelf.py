# Problem 238
from typing import List


class ProductOfArrayExceptSelf:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        nonzeroproduct = 1
        numzeroes = 0

        for i in nums:
            if i == 0:
                numzeroes += 1
            else:
                nonzeroproduct *= i

        if numzeroes > 1:
            return [0] * len(nums)
        else:
            res = []
            for i in nums:
                if i == 0:
                    res.append(nonzeroproduct)
                else:
                    if numzeroes > 0:
                        res.append(0)
                    else:
                        res.append((int)(nonzeroproduct / i))
        return res
