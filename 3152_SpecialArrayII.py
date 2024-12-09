# 3152. Special Array II
import itertools
import operator
from typing import List


class SpecialArrayII:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        # May 2024
        num_invalid = [0] * len(nums)
        for idx in range(1, len(nums)):
            if (nums[idx] + nums[idx - 1]) % 2 == 0:
                num_invalid[idx] = num_invalid[idx - 1] + 1
            else:
                num_invalid[idx] = num_invalid[idx - 1]

        result = []
        for query in queries:
            if (num_invalid[query[1]] - num_invalid[query[0]]) != 0:
                result.append(False)
            else:
                result.append(True)

        return result

    def isArraySpecial2(self, nums: List[int], queries: List[List[int]]) -> List[bool]:\
        # Dec 2024
        flags = [int(not (nums[i] ^ nums[i + 1]) & 1) for i in range(len(nums) - 1)]
        prefix = [0] + list(itertools.accumulate(flags, operator.add))
        return [True if prefix[e] - prefix[s] == 0 else False for [s, e] in queries]


if __name__ == '__main__':
    w = SpecialArrayII()
    print(w.isArraySpecial([3, 7, 8], [[0, 2]]))
    print(w.isArraySpecial([9, 5, 9], [[0, 2]]))
