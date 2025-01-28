# Problem 2658
from typing import List


class MaxNumOfFishInGrid:

    def findMaxFish(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] > 0:
                    val = self.get_val(grid, r, c)
                    res = max(res, val)
        return res

    def get_val(self, grid: List[List[int]], r: int, c: int):
        rows, cols = len(grid), len(grid[0])
        temp = 0

        def get_neis(r, c):
            neis = []
            if r > 0 and grid[r - 1][c] > 0:
                neis.append((r - 1, c))
            if r < rows - 1 and grid[r + 1][c] > 0:
                neis.append((r + 1, c))
            if c > 0 and grid[r][c - 1] > 0:
                neis.append((r, c - 1))
            if c < cols - 1 and grid[r][c + 1] > 0:
                neis.append((r, c + 1))
            return neis

        q = [(r, c)]
        while q:
            (x, y) = q.pop()
            if grid[x][y] > 0:
                temp += grid[x][y]
                grid[x][y] = -grid[x][y]
                neis = get_neis(x, y)
                q = neis + q
        return temp


if __name__ == '__main__':
    m = MaxNumOfFishInGrid()
    print(m.findMaxFish([[8, 6], [2, 6]]))
