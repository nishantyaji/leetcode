# Problem 959
from typing import List


class RegionsCutBySlashes:
    def regionsBySlashes(self, grid: List[str]) -> int:
        # Got this hint
        # Transform
        # space to
        # 0  0  0
        # 0  0  0
        # 0  0  0
        #
        # / to
        # 0  0  1
        # 0  1  0
        # 1  0  0
        #
        # \ to
        # 1  0  0
        # 0  1  0
        # 0  0  1

        rows, cols = 3 * len(grid), 3 * len(grid[0])
        new_grid = [['0' for c in range(cols)] for r in range(rows)]
        for r, s in enumerate(grid):
            for c, ch in enumerate(s):
                if ch == "/":
                    new_grid[3 * r + 2][3 * c] = '1'
                    new_grid[3 * r + 1][3 * c + 1] = '1'
                    new_grid[3 * r][3 * c + 2] = '1'
                elif ch == "\\":
                    new_grid[3 * r][3 * c] = '1'
                    new_grid[3 * r + 1][3 * c + 1] = '1'
                    new_grid[3 * r + 2][3 * c + 2] = '1'
        return self.numIslands(new_grid)

    def numIslands(self, grid: List[List[str]]) -> int:
        # This solution has been copied from my solution to Problem 200
        # Refer file: 0200_NumberOfIslands.py
        isle = '0'
        rows, cols = len(grid), len(grid[0])

        def get_neighbours(r: int, c: int, visited: str):
            neighbours = []
            if r > 0 and grid[r - 1][c] == isle:
                grid[r - 1][c] = visited
                neighbours.append([r - 1, c])
            if c > 0 and grid[r][c - 1] == isle:
                grid[r][c - 1] = visited
                neighbours.append([r, c - 1])
            if r < rows - 1 and grid[r + 1][c] == isle:
                grid[r + 1][c] = visited
                neighbours.append([r + 1, c])
            if c < cols - 1 and grid[r][c + 1] == isle:
                grid[r][c + 1] = visited
                neighbours.append([r, c + 1])
            return neighbours

        isle_count = 0
        for row in range(0, rows):
            for col in range(0, cols):
                if grid[row][col] == isle:
                    isle_count += 1
                    eval_list = [[row, col]]
                    grid[row][col] = str(isle_count + 1)
                    while len(eval_list) > 0:
                        [temp_row, temp_col] = eval_list[0]
                        del eval_list[0]
                        neighbours = get_neighbours(temp_row, temp_col, str(isle_count + 1))
                        eval_list = eval_list + neighbours

        return isle_count


if __name__ == '__main__':
    r = RegionsCutBySlashes()
    print(r.regionsBySlashes([" /", "/ "]))
    # 2
    print(r.regionsBySlashes([" /", "  "]))
    # 1
    print(r.regionsBySlashes(["/\\", "\\/"]))
    # 5
