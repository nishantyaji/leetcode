# Problem 3371
import collections
from typing import List


class IdentifyLargestOutlierInArray:
    def getLargestOutlier(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        total = sum(nums)
        nums.sort()

        for i in range(len(nums) - 1, -1, -1):
            oth, sp_sum = total - nums[i], (total - nums[i]) // 2
            if oth % 2 == 0 and ((sp_sum == nums[i] and counter[sp_sum] == 2)
                                 or (sp_sum != nums[i] and sp_sum in counter)):
                return nums[i]
        return nums[0]
