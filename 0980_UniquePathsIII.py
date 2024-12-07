# Problem 980
import copy
from typing import List


class UniquePathsIII:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        global start, end
        rows, cols = len(grid), len(grid[0])
        obstacles = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    start = (r, c)
                elif grid[r][c] == 2:
                    end = (r, c)
                elif grid[r][c] == -1:
                    obstacles.add((r, c))

        visited = set()
        res = [0]
        self.recurse(visited, obstacles, start, end, grid, res)
        return res[0]

    def recurse(self, visited, obstacles, s, e, grid, res):
        rows, cols = len(grid), len(grid[0])

        def get_neis(rr, cc):
            neis = []
            if rr > 0:
                neis.append((rr - 1, cc))
            if rr < rows - 1:
                neis.append((rr + 1, cc))
            if cc > 0:
                neis.append((rr, cc - 1))
            if cc < cols - 1:
                neis.append((rr, cc + 1))
            return [n for n in neis if n not in visited and n not in obstacles]

        for nei in get_neis(s[0], s[1]):
            visited_copy = copy.deepcopy(visited)
            visited_copy.add(s)
            if nei == e:
                if rows * cols - len(obstacles) == len(visited_copy) + 1:
                    res[0] += 1
            self.recurse(visited_copy, obstacles, nei, end, grid, res)


if __name__ == '__main__':
    u = UniquePathsIII()
    print(u.uniquePathsIII([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]))  # 2
    print(u.uniquePathsIII([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]]))  # 4
    print(u.uniquePathsIII([[0, 1], [2, 0]]))  # 0
