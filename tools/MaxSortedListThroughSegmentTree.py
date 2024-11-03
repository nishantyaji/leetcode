# SortedDict using segment tree
# Check Codeforces 2009 (970 Div 4) Problem G1
class SegmentTree:
    def __init__(self, size: int):
        # size = size of compressed map (= 1 + max_elem_of_compressed_map)
        self.size = size
        self.st = [0] * (4 * size)
        self.invalid = -100001

    def seg_op(self, left: int, right: int) -> int:
        return max([left, right])

    def update(self, place: int, val: int):
        self._update_(0, 0, self.size, place, val)

    def _update_(self, index: int, low: int, high: int, place: int, val: int):
        if low == high:
            self.st[index] = self.st[index] + val
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


class MaxSortedListThroughSegmentTree:

    def __init__(self, arr: list[int]):
        self.arr = arr
        arr_set = sorted(set(arr))
        self.seg = SegmentTree(len(arr_set))
        self.compress = {x: i for i, x in enumerate(arr_set)}

    def add_key(self, key: int):
        self.seg.update(self.compress[key], 1)

    def rem_key(self, key: int):
        self.seg.update(self.compress[key], -1)

    def max_key(self):
        return self.seg.query(0, self.seg.size + 1)


if __name__ == '__main__':
    arr = [6, 1, 1, 2, 2, 3, 7, 8, 9, 4, 5, 5]
    m = MaxSortedListThroughSegmentTree(arr)
    k = 5
    for i in range(k):
        m.add_key(arr[i])
    for i in range(k, len(arr)):
        to_rem = arr[i - k]
        m.rem_key(to_rem)
        m.add_key(arr[i])
        print(m.max_key())
        # print(k - m.max_key())
