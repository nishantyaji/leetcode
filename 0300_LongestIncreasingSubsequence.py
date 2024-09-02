# Problem 300
from typing import List


class LongestIncreasingSubsequence:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Use coordinate compression to avoid TLE and MLE
        compressed_map = {num: index + 1 for index, num in enumerate(sorted(set(nums)))}

        st = SegmentTree(len(compressed_map))
        for n in nums:
            val = st.query(0, compressed_map[n] - 1)
            st.update(compressed_map[n], 1 + val)

        return st.query(0, len(nums) + 1)


class SegmentTree:
    def __init__(self, size: int):
        self.size = size
        self.st = [0] * (4 * size)
        self.invalid = -100001

    def seg_op(self, left: int, right: int) -> int:
        return max([left, right])

    def update(self, place: int, val: int):
        self._update_(0, 0, self.size, place, val)

    def _update_(self, index: int, low: int, high: int, place: int, val: int):
        if low == high:
            self.st[index] = max(self.st[index], val)
            return
        mid = (low + high) // 2
        if low <= place <= mid:
            self._update_(2 * index + 1, low, mid, place, val)
        else:
            self._update_(2 * index + 2, mid + 1, high, place, val)

        self.st[index] = self.seg_op(self.st[2 * index + 1], self.st[2 * index + 2])

    def query(self, l_query: int, r_query: int):
        return self._query_(0, 0, self.size, l_query, r_query)

    def _query_(self, index: int, low: int, high: int, l_query: int, r_query: int):
        if low >= l_query and high <= r_query:
            return self.st[index]
        if high < l_query or low > r_query:
            return self.invalid
        mid = (low + high) // 2
        low_val = self._query_(2 * index + 1, low, mid, l_query, r_query)
        high_val = self._query_(2 * index + 2, mid + 1, high, l_query, r_query)
        return self.seg_op(low_val, high_val)


if __name__ == '__main__':
    l = LongestIncreasingSubsequence()
    print(l.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]))  # 1
    print(l.lengthOfLIS([0, 1, 0, 3, 2, 3]))  # 4
    print(l.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))  # 4
