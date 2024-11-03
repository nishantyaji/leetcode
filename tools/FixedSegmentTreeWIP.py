class SegmentTree:
    def __init__(self, size: int):
        # size = size of compressed map (= 1 + max_elem_of_compressed_map)
        self.size = size
        self.st = [0] * (4 * size)
        self.invalid = -100001

    def build(self, nums: list[int]):
        self._build_(0, 0, self.size, nums)

    def _build_(self, index: int, low: int, high: int, nums: list[int]):
        if low == high:
            # self.st[index] = nums[low]
            self.st[index] = self.unary_op(self.st[index], nums[low])
            return

        mid = (low + high) // 2
        self._build_(2 * index + 1, low, mid, nums)
        self._build_(2 * index + 2, mid + 1, high, nums)
        self.st[index] = self.seg_op(self.st[2 * index + 1], self.st[2 * index + 2])

    def unary_op(self, existing: int, new: int) -> int:
        return new

    def seg_op(self, left: int, right: int) -> int:
        return max([left, right])

    def update(self, place: int, val: int):
        self._update_(0, 0, self.size, place, val)

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
