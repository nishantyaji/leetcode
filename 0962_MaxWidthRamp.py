# Problem 962
import sys
from typing import List


class SegmentTree:
    def __init__(self, size: int):
        # size = size of compressed map (= 1 + max_elem_of_compressed_map)
        self.size = size
        self.st = [sys.maxsize] * (4 * size)
        self.invalid = sys.maxsize

    def seg_op(self, left: int, right: int) -> int:
        return min([left, right])

    def update(self, place: int, val: int):
        self._update_(0, 0, self.size - 1, place, val)

    def _update_(self, index: int, low: int, high: int, place: int, val: int):
        if low == high:
            self.st[index] = min(self.st[index], val)
            return
        mid = (low + high) // 2
        if low <= place <= mid:
            self._update_(2 * index + 1, low, mid, place, val)
        else:
            self._update_(2 * index + 2, mid + 1, high, place, val)

        self.st[index] = self.seg_op(self.st[2 * index + 1], self.st[2 * index + 2])

    def query(self, l_query: int, r_query: int):
        return self._query_(0, 0, self.size - 1, l_query, r_query)

    def _query_(self, index: int, low: int, high: int, l_query: int, r_query: int):
        if low >= l_query and high <= r_query:
            return self.st[index]
        if high < l_query or low > r_query:
            return self.invalid
        mid = (low + high) // 2
        low_val = self._query_(2 * index + 1, low, mid, l_query, r_query)
        high_val = self._query_(2 * index + 2, mid + 1, high, l_query, r_query)
        return self.seg_op(low_val, high_val)


class MaxWidthRamp:

    def maxWidthRamp(self, nums: List[int]) -> int:
        # This approach uses the segment tree approach.
        # This approach has the time complexity of O(nlogn)
        # There are better approaches i.e. time complexity O(n)
        # Refer: https://leetcode.com/problems/maximum-width-ramp/editorial/?envType=daily-question&envId=2024-10-10
        # There are videos on youtube with the solution in O(n)
        co_map = {x: i for i, x in enumerate(sorted(set(nums)))}
        st = SegmentTree(len(co_map))
        res = 0
        for i, n in enumerate(nums):
            ans = st.query(0, co_map[n])
            if ans != sys.maxsize:
                res = max(res, (i - ans))
            st.update(co_map[n], i)
        return res


if __name__ == '__main__':
    m = MaxWidthRamp()
    print(m.maxWidthRamp([6, 0, 8, 2, 1, 5]))
    print(m.maxWidthRamp([9, 8, 1, 0, 1, 9, 4, 0, 4, 1]))
