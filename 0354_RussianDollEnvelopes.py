# Problem 354

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


class RussianDollEnvelopes2:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], x[1]))
        y_set = sorted(set(map(lambda x: x[1], envelopes)))
        comp = {x: i + 2 for i, x in enumerate(y_set)}
        st = SegmentTree(len(y_set) + 2)

        res, prev = 0, -1
        update_q = ()
        for i in range(len(envelopes)):
            if envelopes[i][0] != prev:
                for q in update_q:
                    # st.update(comp[envelopes[i][1]], temp + 1)
                    st.update(q[0], q[1])
                update_q = []
            temp = st.query(0, comp[envelopes[i][1]] - 1)
            prev = envelopes[i][0]
            res = max(temp + 1, res)
            update_q.append([comp[envelopes[i][1]], temp + 1])

        return res


if __name__ == '__main__':
    r = RussianDollEnvelopes2()
    print(r.maxEnvelopes([[1, 1], [1, 1], [1, 1]]))  # 1
    print(r.maxEnvelopes([[5, 4], [6, 4], [6, 7], [2, 3]]))  # 3
    print(r.maxEnvelopes([[4, 5], [4, 6], [6, 7], [2, 3], [1, 1]]))  # 4
    print(r.maxEnvelopes([[8, 3], [3, 20], [15, 5], [11, 2], [
        19, 6], [9, 18], [1, 19], [13, 3], [14, 20], [6, 7]]))
    print(r.maxEnvelopes([[5, 5], [5, 5], [5, 5], [5, 5]]))

    print(r.maxEnvelopes(
        [[21, 33], [27, 39], [6, 29], [45, 2], [5, 16], [14, 15],
         [31, 31], [28, 43], [14, 13], [44, 29], [44, 47], [26, 1],
         [40, 18], [33, 6], [39, 40], [39, 13], [1, 33], [31, 4],
         [21, 40], [50, 14], [17, 44], [21, 22], [32, 41], [18, 28],
         [29, 50], [9, 24], [25, 26], [32, 30], [17, 32], [21, 2], [17, 39]]

    ))
