# Problem 2435
from typing import List


class PathsInMatrixWhoseSumIsDivisibleByK:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        rows, cols, base = len(grid), len(grid[0]), 1000000007
        vals = [[[0 for _ in range(k)] for _ in range(cols)] for _ in range(rows)]
        vals[0][0][grid[0][0] % k] = 1

        def recur(r: int, c: int):
            this_val = grid[r][c]
            for i in range(k):
                if r - 1 >= 0:
                    vals[r][c][(i + this_val) % k] = (vals[r][c][(i + this_val) % k] + vals[r - 1][c][i]) % base
                if c - 1 >= 0:
                    vals[r][c][(i + this_val) % k] = (vals[r][c][(i + this_val) % k] + vals[r][c - 1][i]) % base

        for i in range(1, cols):
            recur(0, i)
        for i in range(1, rows):
            recur(i, 0)

        for i in range(1, rows):
            for j in range(1, cols):
                recur(i, j)

        return vals[rows - 1][cols - 1][0] % base
