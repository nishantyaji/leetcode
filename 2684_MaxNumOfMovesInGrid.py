# Problem 2684
import functools
from typing import List


class MaxNumOfMovesInGrid:
    def maxMoves(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dp = [[[False for _ in range(3)] for _ in range(cols)] for _ in range(rows)]
        for r in range(rows):
            for c in range(0, cols - 1):
                for d in range(max(0, r - 1), min(rows, r + 2)):
                    if grid[r][c] < grid[d][c + 1]:
                        dp[r][c][d - r] = True

        # DFS
        @functools.cache
        def traverse(rx, cx) -> int:
            this_len = 0
            for rd in range(max(0, rx - 1), min(rows, rx + 2)):
                i = rd - rx
                if dp[rx][cx][i]:
                    if cx + 1 == cols:
                        return 1
                    temp_len = 1 + traverse(rx + i, cx + 1)
                    this_len = max(temp_len, this_len)
            return this_len

        max_len = -1
        for row in range(rows):
            max_len = max(max_len, traverse(row, 0))
        return max_len


if __name__ == '__main__':
    m = MaxNumOfMovesInGrid()
    print(m.maxMoves([[2, 4, 3, 5], [5, 4, 9, 3], [3, 4, 2, 11], [10, 9, 13, 15]]))
    print(m.maxMoves([[3, 2, 4], [2, 1, 9], [1, 1, 7]]))
