# Problem 1964
from typing import List


class SegmentTree:
    def __init__(self, size: int):
        # size = size of compressed map (= 1 + max_elem_of_compressed_map)
        self.size = size
        self.st = [0] * (4 * size)
        self.invalid = -100001

    def seg_op(self, left: int, right: int) -> int:
        return max([left, right])

    def update(self, place: int, val: int):
        self._update_(0, 0, self.size - 1, place, val)

    def _update_(self, index: int, low: int, high: int, place: int, val: int):
        if low == high:
            # use unary_op below
            self.st[index] = max(self.st[index], val)
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



class FindLongestValidObstacleCourseAtEachPosition:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        # can be solved easily with bisect functions (also has lesser run time)
        uniq = sorted(set(obstacles))
        comp = {x: i + 2 for i, x in enumerate(uniq)}
        st = SegmentTree(len(comp) + 2)
        res = [0] * len(obstacles)
        for i, o in enumerate(obstacles):
            temp = st.query(0, comp[o])
            res[i] = temp + 1
            st.update(comp[o], temp + 1)

        return res


if __name__ == '__main__':
    f = FindLongestValidObstacleCourseAtEachPosition()
    print(f.longestObstacleCourseAtEachPosition([1,2,3,2]))   # [1, 2, 3, 3]
    print(f.longestObstacleCourseAtEachPosition([2,2,1]))   # [1, 2, 1]
    print(f.longestObstacleCourseAtEachPosition([3,1,5,6,4,2]))   # [1, 1, 2, 3, 2, 2]