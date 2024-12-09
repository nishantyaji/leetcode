# Problem 3381
import sys
from typing import List


class MaxSubArraySumWithLengthDivisibleByK:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        # Modified Kadane
        rolling = [0] * (len(nums) - k + 1)
        rolling[0] = sum(nums[:k])
        for i in range(1, len(rolling)):
            rolling[i] = rolling[i - 1] - nums[i - 1] + nums[i + k - 1]

        cur_max_sum, max_sum = [-sys.maxsize] * k, [-sys.maxsize] * k
        for index, r in enumerate(rolling):
            cur_max_sum[index % k] = max(cur_max_sum[index % k] + r, r)
            max_sum[index % k] = max(max_sum[index % k], cur_max_sum[index % k])
        return max(max_sum)


if __name__ == '__main__':
    m = MaxSubArraySumWithLengthDivisibleByK()
    print(m.maxSubarraySum([1, 2], 1))  # 3
    print(m.maxSubarraySum([-1, -2, -3, -4, -5], 4))  # -10
    print(m.maxSubarraySum([-5, 1, 2, -3, 4], 2))  # 4
