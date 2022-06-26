# Problem 1752
from typing import List


class CheckIfArrayIsSortedAndRotated:
    def check(self, nums: List[int]) -> bool:
        min_idx = 0
        if nums[0] >= nums[-1]:
            prev = nums[0]
            counter = 0
            for num in nums[1:]:
                counter = counter + 1
                if num < prev:
                    min_idx = counter
                    break
                prev = num

        for i in range(1, len(nums)):
            if nums[(i + min_idx) % len(nums)] < nums[(i - 1 + min_idx) % len(nums)]:
                return False
        return True


if __name__ == '__main__':
    c = CheckIfArrayIsSortedAndRotated()
    print(c.check([6, 10, 6]))
    print(c.check([1, 1, 1]))
    print(c.check([3, 4, 5, 1, 2]))
    print(c.check([2, 1, 3, 4]))
    print(c.check([1, 2, 3]))
