# Problem 703
from typing import List


class KthLargestElemInStream:

    def __init__(self, k: int, nums: List[int]):
        self.limit = k
        self.intern = nums
        self.intern.sort(reverse=True)
        if len(nums):
            self.intern = self.intern[:k]

    def add(self, val: int) -> int:
        if len(self.intern) == self.limit and val < self.intern[-1]:
            return self.intern[-1]

        start, end = 0, len(self.intern) - 1
        while start <= end:
            mid = (start + end) // 2
            if self.intern[mid] == val:
                start = mid
                break
            elif self.intern[mid] < val:
                end = mid - 1
            else:
                start = mid + 1

        self.intern = self.intern[:start] + [val] + self.intern[start:]
        self.intern = self.intern[:self.limit]
        return self.intern[-1]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
