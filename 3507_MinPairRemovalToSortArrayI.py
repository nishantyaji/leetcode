# Problem 3507
import sys
from typing import List


class MinPairRemovalToSortArrayI:

    def minimumPairRemoval(self, nums: List[int]) -> int:

        def is_sorted(arr: List[int]):
            for i in range(0, len(arr) - 1):
                if arr[i] > arr[i + 1]:
                    return False
            return True

        res = 0
        while not is_sorted(nums):
            res += 1
            min_sum, index = sys.maxsize, -1
            for i in range(0, len(nums) - 1):
                if nums[i] + nums[i + 1] < min_sum:
                    min_sum = nums[i] + nums[i + 1]
                    index = i
            nums = nums[:index] + [min_sum] + nums[index + 2:]

        return res


if __name__ == '__main__':
    m = MinPairRemovalToSortArrayI()
    print(m.minimumPairRemoval([5, 2, 3, 1]))
    print(m.minimumPairRemoval([1, 2, 2]))
