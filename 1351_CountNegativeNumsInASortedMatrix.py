# Problem 1351
from typing import List


class CountNegativeNumsInASortedMatrix:

    def countNegatives(self, grid: List[List[int]]) -> int:
        rows, cols, res = len(grid), len(grid[0]), 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] < 0:
                    res += 1
        return res