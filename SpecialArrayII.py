# 3152. Special Array II

from typing import List


class SpecialArrayII:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
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


if __name__ == '__main__':
    w = SpecialArrayII()
    print(w.isArraySpecial([3, 7, 8], [[0, 2]]))
    print(w.isArraySpecial([9, 5, 9], [[0, 2]]))
