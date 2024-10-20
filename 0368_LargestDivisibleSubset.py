# Problem 368
from typing import List


class LargestDivisibleSubset:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp = [0] * len(nums)
        for i in range(len(nums)):
            dp[i] = {nums[i]}

        max_len, res = 1, {nums[0]}
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] % nums[i] == 0:
                    temp = {nums[j]}.union(dp[i])
                    if len(temp) > len(dp[j]):
                        dp[j] = temp
                        if len(dp[j]) > max_len:
                            max_len = len(dp[j])
                            res = dp[j]
        return list(res)


if __name__ == '__main__':
    l = LargestDivisibleSubset()
    print(l.largestDivisibleSubset([4, 8, 10, 240]))
