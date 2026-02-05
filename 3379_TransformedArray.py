# Problem 3379
from typing import List


class TransformedArray:

    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        def get_val(idx: int):
            return nums[(((idx + nums[idx]) % n) + n) % n]

        return list(map(get_val, range(n)))
