# Problem 2780
import collections
from typing import List


class MinIndexOfValidSplit:

    def minimumIndex(self, nums: List[int]) -> int:
        cntr = collections.Counter(nums)
        [dominant] = [k for k, v in cntr.items() if v > len(nums) // 2]
        dom, val = 0, cntr[dominant]
        for i, x in enumerate(nums):
            dom += (1 if x == dominant else 0)
            is_pre_valid = dom > (i + 1) // 2
            is_post_valid = (val - dom) > (len(nums) - i - 1) // 2
            if is_pre_valid and is_post_valid:
                return i
        return -1


if __name__ == '__main__':
    m = MinIndexOfValidSplit()
    print(m.minimumIndex([1, 2, 2, 2]))  # 2
    print(m.minimumIndex([2, 1, 3, 1, 1, 1, 7, 1, 2, 1]))  # 4
    print(m.minimumIndex([3, 3, 3, 3, 7, 2, 2]))  # -1
