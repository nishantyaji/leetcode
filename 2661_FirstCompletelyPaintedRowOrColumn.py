# Problem 2661
from typing import List


class FirstCompletelyPaintedRowOrColumn:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        rows, cols = len(mat), len(mat[0])
        row_set, col_set, mp = [0 for _ in range(rows)], [0 for _ in range(cols)], {}
        for i in range(rows):
            for j in range(cols):
                row_set[i] += 1
                col_set[j] += 1
                mp[mat[i][j]] = (i, j)

        for i, a in enumerate(arr):
            x, y = mp[a]
            row_set[x] -= 1
            if not row_set[x]:
                return i
            col_set[y] -= 1
            if not col_set[y]:
                return i
        return rows * cols - 1
