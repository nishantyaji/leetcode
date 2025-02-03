# Problem 3105
from typing import List


class LongestStrictlyIncreasingOrDecreasingSubarray:

    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        prev, cumu, res = nums[0], 1, -1
        for i in range(1, len(nums)):
            res = max(abs(cumu), res)
            if nums[i] > prev:
                if cumu <= 0:
                    cumu = 2
                else:
                    cumu += 1
            elif nums[i] < prev:
                if cumu >= 0:
                    cumu = -2
                else:
                    cumu -= 1
            else:
                cumu = 0
            prev = nums[i]
        return max(abs(cumu), res)


if __name__ == '__main__':
    l = LongestStrictlyIncreasingOrDecreasingSubarray()
    print(l.longestMonotonicSubarray([1,4,3,3,2]))
    print(l.longestMonotonicSubarray([3, 2, 1]))
