# Problem 2164
from typing import List


class SortEvenAndOddIndicesIndependently:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        for i in range(0, len(nums)):
            for j in range(i+2, len(nums), 2):
                if i % 2 == 0 and nums[i] > nums[j]:
                    self.swap(nums, i, j)
                elif i % 2 == 1 and nums[i] < nums[j]:
                    self.swap(nums, i, j)
        return nums

    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp


if __name__ == '__main__':
    s = SortEvenAndOddIndicesIndependently()
    print(s.sortEvenOdd([4,1,2,3]))