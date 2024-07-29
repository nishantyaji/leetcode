# Problem 1395
import bisect
from typing import List


class CountNumOfTeams:
    def numTeams(self, rating: List[int]) -> int:
        temp1, temp2 = [], []
        small_b, large_b, small_a, large_a = [], [], [], []
        for i, r in enumerate(rating):
            idx = self.ins(temp1, r)
            small_b.append(idx)
            large_b.append(i - idx)
        for i, r in enumerate(rating[::-1]):
            idx = self.ins(temp2, r)
            small_a.append(idx)
            large_a.append(i - idx)
        small_a.reverse()
        large_a.reverse()
        res = 0
        for i, r in enumerate(rating):
            res += (small_b[i] * large_a[i])
            res += (large_b[i] * small_a[i])
        return res

    def ins(self, arr: List[int], n: int) -> int:
        idx = bisect.bisect_left(arr, n)
        bisect.insort_left(arr, n)
        return idx


if __name__ == '__main__':
    c = CountNumOfTeams()
    print(c.numTeams([2, 5, 3, 4, 1]))
    print(c.numTeams([2, 1, 3]))
    print(c.numTeams([1, 2, 3, 4]))
