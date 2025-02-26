# Problem 1749
from typing import List


class MaxAbsSumOfAnySubarray:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        # Similar to Kadane
        res, high_res, low_res, run_res = 0, 0, 0, 0
        for n in nums:
            run_res += n
            if run_res < low_res:
                low_res = run_res
            elif run_res > high_res:
                high_res = run_res

            if run_res < 0:
                temp = abs(run_res - high_res)
            else:
                temp = abs(run_res - low_res)
            res = max(res, temp)
        return res


if __name__ == '__main__':
    m = MaxAbsSumOfAnySubarray()
    print(m.maxAbsoluteSum([1, -3, 2, 3, -4]))  # 5
    print(m.maxAbsoluteSum([2, -5, 1, -4, 3, -2]))  # 8
