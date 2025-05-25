# Problem 73
from typing import List


class SetMatrixZeroes:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_zeros, col_zeros = set(), set()
        rows, cols = len(matrix), len(matrix[0])
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    row_zeros.add(r)
                    col_zeros.add(c)

        for r in range(rows):
            for c in range(cols):
                if r in row_zeros or c in col_zeros:
                    matrix[r][c] = 0
