# Problem 3282
from typing import List


class ReachEndOfArrayWithMaxScore:
    def findMaximumScore(self, nums: List[int]) -> int:
        prev, prev_idx = nums[0], 0

        res = 0
        for i, n in enumerate(nums[1:-1]):
            if n > prev:
                res += prev * (i + 1 - prev_idx)
                prev, prev_idx = n, i + 1
        res += (len(nums) - 1 - prev_idx) * prev
        return res


if __name__ == '__main__':
    r = ReachEndOfArrayWithMaxScore()
    print(r.findMaximumScore([1, 3, 1, 5]))
    print(r.findMaximumScore([4, 3, 1, 3, 2]))
