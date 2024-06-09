# Problem 315
from typing import List

# Use this template for Binary Indexed Tree (BIT)) or Fenwick Tree
class BIT:
    def __init__(self, size: int):
        self.n = size
        self.bit = [0] * (size + 1)

    def update(self, place: int, val: int):
        while place <= self.n:
            self.bit[place] += val
            place += (place & -place)

    def query(self, place: int):
        result = 0
        while place > 0:
            result += self.bit[place]
            place -= (place & -place)
        return result


class CountOfSmallNumAfterSelf:
    def countSmaller(self, nums: List[int]) -> List[int]:
        # Transform the array so that we can deal with BIT
        # i.e. 1-indexed
        min_val = min(nums)
        if min_val <= 0:
            nums = list(map(lambda x: x - (min_val - 1), nums))
        # Let's see if we can reduce this memory
        fenwick = BIT(max(nums))
        result = [0] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            fenwick.update(nums[i], 1)
            # number in range (0, nums[i]-1)
            # because the query is on strictly greater
            result[i] = fenwick.query(nums[i] - 1)
        return result


if __name__ == '__main__':
    c = CountOfSmallNumAfterSelf()
    print(c.countSmaller([5, 2, 6, 1]))
    print(c.countSmaller([-1]))
    print(c.countSmaller([-1, -1]))
