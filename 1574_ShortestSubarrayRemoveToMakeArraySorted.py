# Problem 1574
import bisect
import sys
from typing import List


class ShortestSubarrayRemoveToMakeArraySorted:

    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        # O(n) complexity
        sq, eq = [arr[0]], [arr[-1]]
        for i in range(1, len(arr)):
            if arr[i] < arr[i-1]:
                break
            sq.append(arr[i])
        for j in range(1, len(arr)):
            if arr[len(arr) - j] < arr[len(arr) - j - 1]:
                break
            eq.append(arr[len(arr) - j - 1])

        if len(sq) == len(arr):
            return 0
        max_len, eq = max(len(sq), len(eq)), eq[::-1]
        es = bisect.bisect_left(eq, sq[0])
        for i in range(len(sq)):
            while es < len(eq) and eq[es] < sq[i]:
                es += 1
            max_len = max(max_len, i + len(eq) - es + 1)
        return len(arr) - max_len

    def findLengthOfShortestSubarray2(self, arr: List[int]) -> int:
        # O(nlogn) complexity
        s, e = 0, len(arr) - 1
        sq, eq = [], []

        prev = -1
        while s < len(arr) and arr[s] >= prev:
            sq.append(arr[s])
            prev = arr[s]
            s += 1

        if len(sq) == len(arr):
            return 0

        prev = sys.maxsize
        while e >= 0 and arr[e] <= prev:
            eq.append(arr[e])
            prev = arr[e]
            e -= 1

        max_len = len(sq)  # When we consider just the start
        for i, e in enumerate(eq[::-1]):
            s_idx = bisect.bisect_right(sq, e)
            max_len = max(max_len, s_idx + len(eq) - i)
        return len(arr) - max_len


if __name__ == '__main__':
    s = ShortestSubarrayRemoveToMakeArraySorted()
    print(s.findLengthOfShortestSubarray([36, 6, 1, 19, 26, 24, 27, 34, 2, 16, 31, 10, 8, 2, 10, 14, 29, 35, 37]))  # 13
    print(s.findLengthOfShortestSubarray([16, 10, 0, 3, 22, 1, 14, 7, 1, 12, 15]))  # 8
    print(s.findLengthOfShortestSubarray([1, 2, 3]))  # 0
    print(s.findLengthOfShortestSubarray([2, 2, 2, 1, 1, 1]))  # 3
    print(s.findLengthOfShortestSubarray([10, 13, 17, 21, 15, 15, 9, 17, 22, 22, 13]))  # 7
    print(s.findLengthOfShortestSubarray([1, 2, 3, 10, 4, 2, 3, 5]))  # 3
    print(s.findLengthOfShortestSubarray([5, 4, 3, 2, 1]))  # 4
