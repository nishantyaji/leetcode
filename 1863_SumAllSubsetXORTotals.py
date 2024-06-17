# Problem 1863
from typing import List


class SumAllSubsetXORTotals:
    def __init__(self):
        self.nums = []
        self.full_len = 0
        self.result = 0

    def subsetXORSum(self, nums: List[int]) -> int:
        self.nums = nums
        self.full_len = len(self.nums)
        self.result = 0
        self.recurse(0, 0)
        return self.result

    def recurse(self, index_on: int, run_xor: int):
        for i in range(index_on, self.full_len):
            temp = run_xor ^ self.nums[i]
            self.result += temp
            if i + 1 <= self.full_len - 1:
                self.recurse(i + 1, temp)


if __name__ == '__main__':
    s = SumAllSubsetXORTotals()
    print(s.subsetXORSum([1, 3]))
    print(s.subsetXORSum([5, 1, 6]))
    print(s.subsetXORSum([3, 4, 5, 6, 7, 8]))
