from typing import List


class PeaksInArray:

    ##########################################################################################
    #
    #  Solution using the Segment Tree
    #
    ##########################################################################################
    def countOfPeaks(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        is_left_smaller = [False] * len(nums)
        is_right_smaller = [False] * len(nums)
        is_peak = [False] * len(nums)

        arr = [0] * len(nums)
        for i, n in enumerate(nums):
            is_left_smaller[i] = False if i == 0 else nums[i - 1] < nums[i]
            is_right_smaller[i] = False if i == len(nums) - 1 else nums[i] > nums[i + 1]
            is_peak[i] = is_left_smaller[i] and is_right_smaller[i]
            if is_peak[i]:
                arr[i] = 1

        st = AnotherSegmentTree(len(arr))
        st.build(arr)
        final_result = []
        for q in queries:
            if q[0] == 1:
                left, right = q[1], q[2]
                if left in [right, right - 1]:
                    final_result.append(0)
                else:
                    final_result.append(st.query(0, 0, len(arr) - 1, left + 1, right - 1))
            # query
            elif q[0] == 2:
                index, val = q[1], q[2]
                nums[index] = val

                # when updating an index the peak-ness of even the left and right neighbours are affected
                for j in [-1, 0, 1]:
                    if 0 <= index + j < len(nums):
                        prev_peak = is_peak[index + j]
                        is_left_smaller[index + j] = False if index + j == 0 else nums[index + j - 1] < nums[index + j]
                        is_right_smaller[index + j] = False if index + j == len(nums) - 1 else nums[index + j] > nums[
                            index + j + 1]
                        is_peak[index + j] = is_left_smaller[index + j] and is_right_smaller[index + j]
                        if prev_peak != is_peak[index + j]:
                            st.toggle(index + j, arr)
        return final_result


class AnotherSegmentTree:
    def __init__(self, size: int):
        self.size = size
        self.st = [0] * (4 * size)
        # self.invalid is changed as per op. In this case op is "max"
        self.invalid = -100001

    def build(self, arr: List[int]):
        self._build_(0, 0, len(arr) - 1, arr)

    def _build_(self, index: int, low: int, high: int, arr: List[int]):
        if low == high:
            self.st[index] = arr[low]
            return

        mid = (low + high) // 2
        self._build_(2 * index + 1, low, mid, arr)
        self._build_(2 * index + 2, mid + 1, high, arr)
        self.st[index] = self.seg_op(self.st[2 * index + 1], self.st[2 * index + 2])

    def seg_op(self, left: int, right: int) -> int:
        result = 0
        if left != self.invalid:
            result += left
        if right != self.invalid:
            result += right
        return result

    def toggle(self, place: int, arr: List[int]):
        # akin to a point update
        self._toggle_(0, 0, len(arr) - 1, place)

    def _toggle_(self, index: int, low: int, high: int, place: int):
        if low == high:
            # leaf node - end condition
            self.st[index] = self.st[index] ^ 1
            return
        mid = (low + high) // 2
        if low <= place <= mid:
            self._toggle_(2 * index + 1, low, mid, place)
        else:
            self._toggle_(2 * index + 2, mid + 1, high, place)

        self.st[index] = self.seg_op(self.st[2 * index + 1], self.st[2 * index + 2])

    def query(self, index: int, low: int, high: int, l_query: int, r_query: int):
        if low >= l_query and high <= r_query:
            # node is within the RMQ query bounds
            return self.st[index]
        if high < l_query or low > r_query:
            return self.invalid
        mid = (low + high) // 2
        low_val = self.query(2 * index + 1, low, mid, l_query, r_query)
        high_val = self.query(2 * index + 2, mid + 1, high, l_query, r_query)
        return self.seg_op(low_val, high_val)

    ##########################################################################################
    #
    #  Solution using the standard BIT or Fenwick tree
    #
    ##########################################################################################
    def countOfPeaks_BIT(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        is_left_smaller = [False] * len(nums)
        is_right_smaller = [False] * len(nums)
        is_peak = [False] * len(nums)
        fw = BIT(len(nums))

        arr = [0] * len(nums)
        for i, n in enumerate(nums):
            is_left_smaller[i] = False if i == 0 else nums[i - 1] < nums[i]
            is_right_smaller[i] = False if i == len(nums) - 1 else nums[i] > nums[i + 1]
            is_peak[i] = is_left_smaller[i] and is_right_smaller[i]
            if is_peak[i]:
                arr[i] = 1
                fw.update(i, 1)

        final_result = []
        for q in queries:
            if q[0] == 1:
                left, right = q[1], q[2]
                if left in [right, right - 1]:
                    final_result.append(0)
                else:
                    final_result.append(fw.query(right - 1) - fw.query(left))
            # query
            elif q[0] == 2:
                index, val = q[1], q[2]
                nums[index] = val

                # when updating an index the "peak-ness" of even the left and right neighbours are affected
                for j in [-1, 0, 1]:
                    if 0 <= index + j < len(nums):
                        prev_peak = is_peak[index + j]
                        is_left_smaller[index + j] = False if index + j == 0 else nums[index + j - 1] < nums[index + j]
                        is_right_smaller[index + j] = False if index + j == len(nums) - 1 else nums[index + j] > nums[
                            index + j + 1]
                        is_peak[index + j] = is_left_smaller[index + j] and is_right_smaller[index + j]
                        if prev_peak != is_peak[index + j]:
                            # if now the concerned index is peak and was not before we add 1
                            # if it was peak before and not now we subtract 1
                            val = 1 if is_peak[index + j] else -1
                            fw.update(index + j, val)
        return final_result


class BIT:
    def __init__(self, size: int):
        self.n = size
        self.bit = [0] * (size + 1)

    def update(self, place: int, val: int):
        while place <= self.n:
            self.bit[place] += val
            place += (place & -place)

    def query(self, place: int):
        result = 0
        while place > 0:
            result += self.bit[place]
            place -= (place & -place)
        return result


if __name__ == '__main__':
    w = PeaksInArray()
    print(w.countOfPeaks([8, 5, 9, 3, 5], [[1, 2, 4], [1, 0, 1], [2, 2, 4]]))
    # [0,0]
    print(w.countOfPeaks([4, 9, 4, 10, 7], [[2, 3, 2], [2, 1, 3], [1, 2, 3]]))
    # [0]
    print(w.countOfPeaks([4, 10, 8, 6], [[1, 0, 3], [1, 2, 3], [1, 2, 3]]))
    # [1,0,0]
    print(w.countOfPeaks([9, 9, 3], [[1, 0, 0], [2, 2, 5], [2, 2, 10]]))
    # [0]
    print(w.countOfPeaks([7, 10, 7], [[1, 2, 2], [2, 0, 6], [1, 0, 2]]))
    # [0,1]
    print(w.countOfPeaks([3, 1, 4, 2, 5], [[2, 3, 4], [1, 0, 4]]))
    # [0]
    print(w.countOfPeaks([4, 1, 4, 2, 1, 5], [[2, 2, 4], [1, 0, 2], [1, 0, 4]]))
    # [0,1]
