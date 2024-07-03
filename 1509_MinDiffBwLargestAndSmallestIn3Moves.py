# Problem 1509

from typing import List


class MinDiffBwLargestAndSmallestIn3Moves:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        nums.sort()
        result = 100000000000000009

        temp = nums[1:-2]
        result = min(result, temp[-1] - temp[0])
        temp = nums[0:-3]
        result = min(result, temp[-1] - temp[0])
        temp = nums[3:]
        result = min(result, temp[-1] - temp[0])
        temp = nums[2:-1]
        result = min(result, temp[-1] - temp[0])

        return result


if __name__ == '__main__':
    m = MinDiffBwLargestAndSmallestIn3Moves()
    print(m.minDifference([9, 48, 92, 48, 81, 31]))
    # 17
    print(m.minDifference([5, 3, 2, 4]))
    print(m.minDifference([1, 5, 0, 10, 14]))
    print(m.minDifference([3, 100, 20]))
