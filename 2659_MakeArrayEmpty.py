# Problem 2659
from typing import List


class MakeArrayEmpty:
    def countOperationsToEmptyArray(self, nums: List[int]) -> int:
        index_map = {x: i for i, x in enumerate(nums)}
        nums.sort()
        lenn = len(nums)
        seg = SegmentTree(2 * lenn)

        index = index_map[nums[0]]
        result = lenn
        result += index
        seg.update(index, 1)
        seg.update(lenn + index, 1)
        for n in nums[1:]:
            pres_idx_orig = index_map[n]
            pres_idx = pres_idx_orig + lenn if pres_idx_orig < index else pres_idx_orig
            # We know the elements and indices in the orignal array
            # We know the differences between the indices of consecutive elements (when sorted)
            # but within differences between the indices we should discount the elements that have
            # already been deleted
            #
            # seg-tree update (to 1) counts the number of elements already deleted
            # therefore this for loop should have the numbers sorted
            val = pres_idx - index - seg.query(index, pres_idx)
            result += val
            index = pres_idx_orig
            seg.update(pres_idx_orig, 1)
            seg.update(pres_idx_orig + lenn, 1)

        return result


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
            self.st[index] = nums[low]
            return

        mid = (low + high) // 2
        self._build_(2 * index + 1, low, mid, nums)
        self._build_(2 * index + 2, mid + 1, high, nums)
        self.st[index] = self.seg_op(self.st[2 * index + 1], self.st[2 * index + 2])

    def seg_op(self, left: int, right: int) -> int:
        result = 0
        if left != self.invalid:
            result += left
        if right != self.invalid:
            result += right
        return result

    def update(self, place: int, val: int):
        self._update_(0, 0, self.size, place, val)

    def _update_(self, index: int, low: int, high: int, place: int, val: int):
        if low == high:
            # use unary_op below
            self.st[index] = val
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
    m = MakeArrayEmpty()
    print(m.countOperationsToEmptyArray([-14, -16, -17, 10]))  # 9
    print(m.countOperationsToEmptyArray([1, 2, 4, 3]))  # 5
    print(m.countOperationsToEmptyArray([3, 4, -1]))  # 5
    print(m.countOperationsToEmptyArray([1, 2, 3]))  # 3
