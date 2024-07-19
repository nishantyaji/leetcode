# Problem 1380
from typing import List


class LuckyNumsInMatrix:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        # Yes. I know the number of loops can be decreased.
        rows, cols = len(matrix), len(matrix[0])
        minr, maxc = [], []
        for r in range(rows):
            minr.append(min(matrix[r]))
        for c in range(cols):
            maxc.append(max([matrix[r][c] for r in range(rows)]))

        res = []
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == minr[r] and matrix[r][c] == maxc[c]:
                    res.append(matrix[r][c])
        return res

