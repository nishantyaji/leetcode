# Problem 704

from typing import List


class BinarySearch:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = int((low + high) / 2)
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                low, high = low, mid - 1
            else:
                low, high = mid + 1, high

        return low if 0 <= low < len(nums) and nums[low] == target else -1
