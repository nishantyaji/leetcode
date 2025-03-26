# Problem 2033
import sys
from typing import List


class MinOpsToMakeUniValueGrid:

    def minOperations(self, grid: List[List[int]], x: int) -> int:
        arr, rows, cols, st,  = [], len(grid), len(grid[0]), set()

        for r in range(rows):
            for c in range(cols):
                st.add(grid[r][c] % x)
                arr.append(grid[r][c])

        if len(st) > 1:
            return -1
        arr.sort()
        if len(arr) % 2 == 1:
            return sum([abs(x - arr[len(arr) // 2]) for x in arr]) // x
        else:
            l, h = (len(arr) // 2) - 1, len(arr) // 2
            y = l if arr[l] == arr[h] else l + 1
            return sum([abs(x - arr[y]) for x in arr]) // x


if __name__ == '__main__':
    m = MinOpsToMakeUniValueGrid()
    print(m.minOperations([[980, 476, 644, 56], [644, 140, 812, 308], [812, 812, 896, 560], [728, 476, 56, 812]],
                          84))  # 45
    print(m.minOperations([[931, 128], [639, 712]], 73))
    print(m.minOperations([[2, 4], [6, 8]], 2))
    print(m.minOperations([[1, 5], [2, 3]], 1))
    print(m.minOperations([[1, 2], [3, 4]], 2))
