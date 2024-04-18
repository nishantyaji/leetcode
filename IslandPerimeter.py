# PRoblem 463

from typing import List


class IslandPerimeter:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def sum_cell(r: int, c: int) -> int:
            if grid[r][c] == 0:
                return 0
            boundary = 0
            boundary = boundary + (1 if r == 0 or grid[r - 1][c] == 0 else 0)
            boundary = boundary + (1 if c == 0 or grid[r][c - 1] == 0 else 0)
            boundary = boundary + (1 if r == rows - 1 or grid[r + 1][c] == 0 else 0)
            boundary = boundary + (1 if c == cols - 1 or grid[r][c + 1] == 0 else 0)
            return boundary

        result = 0
        for row in range(0, rows):
            for col in range(0, cols):
                result += sum_cell(row, col)

        return result


if __name__ == '__main__':
    i = IslandPerimeter()
    print(i.islandPerimeter([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]))
    print(i.islandPerimeter([[1]]))
    print(i.islandPerimeter([[1, 0]]))
