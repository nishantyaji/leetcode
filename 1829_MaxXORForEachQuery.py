# Problem 1829
import itertools
import operator
from typing import List


class MaxXORForEachQuery:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        prefix = list(itertools.accumulate(nums, operator.xor, initial=0))
        res, max_num = [], (2 ** maximumBit) - 1
        for i in range(len(prefix) - 1, 0, -1):
            res.append(max_num ^ prefix[i])
        return res

    def getMaximumXor_OneLiner(self, nums: List[int], maximumBit: int) -> List[int]:
        return [((2 ** maximumBit) - 1) ^ i for i in
                list(itertools.accumulate(nums, operator.xor, initial=0))][::-1][:-1]


if __name__ == '__main__':
    m = MaxXORForEachQuery()
    print(m.getMaximumXor([0, 1, 1, 3], 2))
    print(m.getMaximumXor_OneLiner([0, 1, 1, 3], 2))
