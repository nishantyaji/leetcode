# Problem 303
import functools
from typing import List


class NumArray:
    # this is just a modification/wrapper of BIT
    # i.e. Binary Indexed Tree or Fenwick Tree
    def update(self, place: int, val: int):
        while place < len(self.bit):
            self.bit[place] += val
            place += (place & -place)

    @functools.cache
    def query(self, place: int):
        result = 0
        while place > 0:
            result += self.bit[place]
            place -= (place & -place)
        return result

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.bit = [0] * (len(nums) + 1)
        for idx, n in enumerate(nums):
            self.update(idx + 1, n)

    def sumRange(self, left: int, right: int) -> int:
        return self.query(right + 1) - self.query(left)

    # Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
