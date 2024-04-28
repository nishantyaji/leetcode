# Problem 217

from typing import List


class ContainsDuplicate:
    def containsDuplicate(self, nums: List[int]) -> bool:
        my_set = set()
        for n in nums:
            my_set.add(n)
        return len(my_set) != len(nums)
