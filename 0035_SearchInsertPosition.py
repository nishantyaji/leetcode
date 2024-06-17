# Problem 35

from typing import List


class SearchInsertPosition:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = int((low + high) / 2)
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                low, high = low, mid - 1
            else:
                low, high = mid + 1, high

        return low
