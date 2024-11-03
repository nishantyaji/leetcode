in_fn = input
op_fn = print


class SegmentTree:
    def __init__(self, size: int):
        # size = size of compressed map (= 1 + max_elem_of_compressed_map)
        self.size = size
        self.st = [(None, None)] * (4 * size)

    def build(self, nums: list[int]):
        self._build_(0, 0, self.size, nums)

    def _build_(self, index: int, low: int, high: int, nums: list[int]):
        if low == high:
            # self.st[index] = nums[low]
            self.st[index] = (nums[low], nums[low])
            return

        mid = (low + high) // 2
        self._build_(2 * index + 1, low, mid, nums)
        self._build_(2 * index + 2, mid + 1, high, nums)
        self.st[index] = self.seg_op(self.st[2 * index + 1], self.st[2 * index + 2])

    def seg_op(self, left: tuple, right: tuple) -> tuple:
        return self._min_(left[0], right[0]), self._max_(left[1], right[1])

    def _com_(self, a, b):
        if a is None and b is None:
            return None
        elif a is None:
            return b
        elif b is None:
            return a
        return None

    def _min_(self, a, b):
        if a is not None and b is not None:
            return min([a, b])
        else:
            return self._com_(a, b)

    def _max_(self, a, b):
        if a is not None and b is not None:
            return max([a, b])
        else:
            return self._com_(a, b)

    def update(self, place: int, val: int):
        self._update_(0, 0, self.size, place, val)

    def _update_(self, index: int, low: int, high: int, place: int, val: int):
        if low == high:
            # use unary_op below
            self.st[index] = (val, val)
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
            return None, None
        mid = (low + high) // 2
        low_val = self._query_(2 * index + 1, low, mid, l_query, r_query)
        high_val = self._query_(2 * index + 2, mid + 1, high, l_query, r_query)
        return self.seg_op(low_val, high_val)


class SpecialSortedSet:
    def __init__(self, size: int):
        self.st = SegmentTree(size)
        self.sz = size
        self.collection = set()

    def __len__(self):
        return len(self.collection)

    def add(self, element: int):
        self.collection.add(element)
        self.st.update(element, element)

    def remove(self, element: int):
        if element in self.collection:
            self.collection.remove(element)
            self.st.update(element, None)
            return True
        return False

    def bounds_cleaned(self, element) -> list[int]:
        result = []
        t = self.bounds(element)
        if t[0] is not None:
            result.append(t[0])
        if t[1] is not None:
            result.append(t[1])
        return result

    def bounds(self, element) -> tuple:
        l_bound = self.st.query(0, element)[1]
        u_bound = self.st.query(element, self.sz)[0]
        return l_bound, u_bound


def read_int_arr(sep=" ") -> list[int]:
    return list(map(int, in_fn().split(sep)))


[rows, cols, q] = read_int_arr()
queries = []
for _ in range(q):
    queries.append(read_int_arr())

row_sp = []
for r in range(rows):
    ss = SpecialSortedSet(cols)
    for i in range(0, cols):
        ss.add(i)
    row_sp.append(ss)

col_sp = []
for c in range(cols):
    ss = SpecialSortedSet(rows)
    for i in range(0, rows):
        ss.add(i)
    col_sp.append(ss)

for [r, c] in queries:
    r -= 1
    c -= 1
    flag = row_sp[r].remove(c)

    if not flag:
        bonds = row_sp[r].bounds_cleaned(c)
        for b in bonds:
            row_sp[r].remove(b)
            col_sp[b].remove(r)

    flag = col_sp[c].remove(r)
    if not flag:
        bonds = col_sp[c].bounds_cleaned(r)
        for b in bonds:
            col_sp[c].remove(b)
            row_sp[b].remove(c)

res = 0
for i in range(rows):
    res += len(row_sp[i])
op_fn(res)
