# Problem 1671
from typing import List


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


class MinNumRemovalsToMakeMountainArray:

    def minimumMountainRemovals(self, nums: List[int]) -> int:
        my_inf = 1000000001
        comp_map = {num: index + 1 for index, num in enumerate(sorted(set(nums)))}

        st, rev_st = SegmentTree(len(comp_map)), SegmentTree(len(comp_map))
        val, lenn = [0] * len(nums), len(nums)
        for i in range(len(nums)):
            left = st.query(0, comp_map[nums[i]] - 1)
            st.update(comp_map[nums[i]], left + 1)
            right = rev_st.query(0, comp_map[nums[lenn - 1 - i]] - 1)
            rev_st.update(comp_map[nums[lenn - 1 - i]], right + 1)
            # disregard by adding -inf
            # those elements that form a ramp and not a mountain
            # that is they have slope on only one side and not in the other
            val[i] += (left if left else -my_inf)
            val[lenn - 1 - i] += (right if right else -my_inf)

        return lenn - max([x + 1 for x in val])


if __name__ == '__main__':
    m = MinNumRemovalsToMakeMountainArray()
    print(m.minimumMountainRemovals([100, 92, 89, 77, 74, 66, 64, 66, 64]))
    print(m.minimumMountainRemovals([9, 8, 1, 7, 6, 5, 4, 3, 2, 1]))
    print(m.minimumMountainRemovals([1, 3, 1]))
    print(m.minimumMountainRemovals([2, 1, 1, 5, 6, 2, 3, 1]))
