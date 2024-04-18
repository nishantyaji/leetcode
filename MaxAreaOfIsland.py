# Problem 695
from typing import List


class MaxAreaOfIsland:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = 2
        isle = 1
        rows, cols = len(grid), len(grid[0])

        def get_neighbours(r: int, c: int):
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

        max_val = 0
        for row in range(0, rows):
            for col in range(0, cols):
                if grid[row][col] == isle:
                    count = 1
                    evallist = [[row, col]]
                    grid[row][col] = visited
                    while len(evallist) > 0:
                        [row, col] = evallist[0]
                        neighbours = get_neighbours(row, col)
                        count += len(neighbours)
                        del evallist[0]
                        evallist += neighbours
                    max_val = max(max_val, count)
        return max_val


if __name__ == '__main__':
    m = MaxAreaOfIsland()
    print(m.maxAreaOfIsland([[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                             [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                             [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]))
    print(m.maxAreaOfIsland([[0, 0, 0, 0, 0, 0, 0, 0]]))
