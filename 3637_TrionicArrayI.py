# Problem 3637
from typing import List


class TrionicArray:
    def isTrionic(self, nums: List[int]) -> bool:
        flag = 1
        breaks = []
        if len(nums) <= 3:
            return False

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return False
            if flag:
                if nums[i] < nums[i - 1]:
                    breaks.append(i)
                    flag = flag ^ 1
            else:
                if nums[i] > nums[i - 1]:
                    breaks.append(i)
                    flag = flag ^ 1
        print(breaks)
        return len(breaks) == 2 and breaks[0] != 1
