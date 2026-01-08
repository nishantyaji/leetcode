# Problem 1458
import sys
from typing import List


class MaxDotProductOfTwoSubsequences:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        l1, l2 = len(nums1), len(nums2)
        dp = [[-sys.maxsize for _ in range(l2)] for _ in range(l1)]
        dp[0][0] = nums1[0] * nums2[0]

        for j in range(1, l2):
            dp[0][j] = max(dp[0][j - 1], nums1[0] * nums2[j])

        for i in range(1, l1):
            dp[i][0] = max(dp[i - 1][0], nums1[i] * nums2[0])

        for i in range(1, l1):
            for j in range(1, l2):
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1] + nums1[i] * nums2[j], nums1[i] * nums2[j])

        return dp[-1][-1]
