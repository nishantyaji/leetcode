# Problem 2501

import collections
from typing import List


class LongestSquareStreakInArray:
    def longestSquareStreak(self, nums: List[int]) -> int:
        mp = collections.defaultdict(int)
        for n in nums:
            mp[n] = 1
        mx = -1
        for i in range(len(nums) - 1):
            if nums[i] * nums[i] in mp:
                mp[nums[i] * nums[i]] = mp[nums[i]] + 1
                mx = max(mx, mp[nums[i] * nums[i]])
        return mx


if __name__ == '__main__':
    l = LongestSquareStreakInArray()
    print(l.longestSquareStreak([3, 9, 81, 6561]))
