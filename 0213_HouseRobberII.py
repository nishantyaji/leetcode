# Problem 213
from typing import List


class HouseRobberII:
    def rob(self, nums: List[int]) -> int:
        # This implementation, though correct, is not optimum
        # Time complexity can be reduced by half
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)

        dp = [0] * len(nums)

        #  the first house is not chosen
        dp[0], dp[1] = 0, nums[1]
        this_max = max(dp)
        for index, n in enumerate(nums[2:]):
            dp[index + 2] = n + dp[index]
            if index - 1 >= 0:
                dp[index + 2] = max(dp[index + 2], n + dp[index - 1])
            this_max = max(this_max, dp[index + 2])

        # the first house is chosen
        dp[0], dp[1] = nums[0], nums[1]
        this_max = max(dp + [this_max])
        for index, n in enumerate(nums[2:-1]):
            dp[index + 2] = n + dp[index]
            if index - 1 >= 0:
                dp[index + 2] = max(dp[index + 2], n + dp[index - 1])
            this_max = max(this_max, dp[index + 2])
        return this_max


if __name__ == '__main__':
    h = HouseRobberII()
    print(h.rob([4, 1, 2]))
    # 4
    print(h.rob([1, 2, 3, 1]))
    # 4
    print(h.rob([2, 3, 2]))
    # 3
    print(h.rob([1, 2, 3]))
    # 3
