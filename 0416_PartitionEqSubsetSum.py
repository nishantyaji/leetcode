# Problem 416
from typing import List


class PartitionEqSubsetSum:

    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False

        total = total // 2
        dp = []
        for i in range(len(nums) + 1):
            dp.append([False] * (total + 1))

        for i in range(1, len(nums) + 1):
            dp[i][nums[i - 1]] = True

        # 0-1 knapsack
        for i in range(1, 1 + len(nums)):
            for j in range(1, 1 + total):
                dp[i][j] = dp[i][j] or dp[i - 1][j]
                if j >= nums[i - 1]:
                    dp[i][j] = dp[i][j] or dp[i - 1][j - nums[i - 1]]

        return dp[-1][-1]


if __name__ == '__main__':
    p = PartitionEqSubsetSum()
    print(p.canPartition([1, 5, 11, 5]))
    print(p.canPartition([1, 2, 3, 5]))
