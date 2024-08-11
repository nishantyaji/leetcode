# Problem 1568
import copy
from typing import List


class MinNumDaysDisconnectIsland:

    def numIslands(self, grid: List[List[int]]) -> int:
        isle = 1
        rows, cols = len(grid), len(grid[0])

        # This is an easier version of Menger's Theorem

        def get_neighbours(r: int, c: int, visited: int):
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
                    grid[row][col] = isle_count + 1
                    while len(eval_list) > 0:
                        [temp_row, temp_col] = eval_list[0]
                        del eval_list[0]
                        neighbours = get_neighbours(temp_row, temp_col, isle_count + 1)
                        eval_list = eval_list + neighbours

        return isle_count

    def minDays(self, grid: List[List[int]]) -> int:
        gridc = copy.deepcopy(grid)
        num_isles = self.numIslands(gridc)
        if num_isles > 1:
            return 0

        rows, cols = len(grid), len(grid[0])
        num_ones = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    num_ones += 1
        if num_ones <= 2:
            return num_ones

        # The min Days is always two
        # because the corner (having 2 or 3 water facing edges)
        # of an island can be isolated in either 1 or 2 days
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    continue
                gridc = copy.deepcopy(grid)
                gridc[r][c] = 0
                num_isles = self.numIslands(gridc)
                if num_isles > 1:
                    return 1

        return 2


if __name__ == '__main__':
    m = MinNumDaysDisconnectIsland()
    print(m.minDays([[0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]))
    # 2
    print(m.minDays([[1, 1]]))
    # 2
    print(m.minDays([[1, 0, 1, 0]]))
    # 0
