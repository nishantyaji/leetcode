# Problem 3255
from typing import List


class FindPowerOfKSizeSubarrayII:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        n, res, i, count = len(nums), [-1] * (len(nums) - k + 1), 0, 0
        diffs = [nums[i] - nums[i - 1] for i in range(1, n)]
        # arr = [1,2,3,4,3,2,5]
        # diff = [1,1,1,-1,-1,3]
        while i < len(diffs):
            d = diffs[i]
            count = 0 if d != 1 else count + 1
            if count == k - 1:
                res[i + 1 - k + 1] = nums[i - (k-2)] + k - 1
                count -= 1
            i += 1
        return res


if __name__ == '__main__':
    f = FindPowerOfKSizeSubarrayII()
    print(f.resultsArray([1, 2, 3, 4, 3, 2, 5], 3))
    print(f.resultsArray([2, 2, 2, 2, 2], 4))
    print(f.resultsArray([3, 2, 3, 2, 3, 2], 2))
