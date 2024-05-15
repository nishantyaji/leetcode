# Problem 2813

from typing import List


class FindSafestPathInGrid:

    def __init__(self):
        self.grid = [[]]
        self.inf = 401
        self.max_safe = self.inf
        self.rows = 0
        self.cols = 0

    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        self.grid = self.change_grid(grid)
        if self.grid[0][0] == 0 or self.grid[self.rows - 1][self.cols - 1] == 0:
            return 0

        start, end = 0, self.max_safe
        pos_dict = {}
        while start <= end:
            mid = start + (end - start) // 2
            pos_dict[mid] = self.recurse(mid)
            if pos_dict[mid]:
                start = mid + 1
            else:
                end = mid - 1
        return mid if pos_dict[mid] else mid - 1

    def recurse(self, distance: int):
        if self.grid[0][0] < distance or self.grid[self.rows - 1][self.cols - 1] < distance:
            return False

        my_set = set()

        def dfs(r: int, c: int) -> bool:
            if r == self.rows - 1 and c == self.cols - 1:
                return True
            if r - 1 >= 0 and distance <= self.grid[r - 1][c] and (r - 1, c) not in my_set:
                my_set.add((r - 1, c))
                res = dfs(r - 1, c)
                if res:
                    return True
            if r + 1 < self.rows and distance <= self.grid[r + 1][c] and (r + 1, c) not in my_set:
                my_set.add((r + 1, c))
                res = dfs(r + 1, c)
                if res:
                    return True
            if c - 1 >= 0 and distance <= self.grid[r][c - 1] and (r, c - 1) not in my_set:
                my_set.add((r, c - 1))
                res = dfs(r, c - 1)
                if res:
                    return True
            if c + 1 < self.cols and distance <= self.grid[r][c + 1] and (r, c + 1) not in my_set:
                my_set.add((r, c + 1))
                res = dfs(r, c + 1)
                if res:
                    return True
            return False

        return dfs(0, 0)

    def change_grid(self, grid: List[List[int]]) -> List[List[int]]:
        self.rows, self.cols = len(grid), len(grid[0])
        grid_copy = [[self.inf for _ in range(self.cols)] for _ in range(self.rows)]

        thieves = []
        for r in range(self.rows):
            for c in range(self.cols):
                if grid[r][c] == 1:
                    thieves.append([r, c])
                    grid_copy[r][c] = 0

        my_set = set()
        q = list(thieves)
        for thief in thieves:
            my_set.add((thief[0], thief[1]))
        while q:
            [r, c] = q.pop(0)
            if (r - 1, c) not in my_set and r - 1 >= 0 and grid[r - 1][c] == 0:
                grid_copy[r - 1][c] = min(grid_copy[r - 1][c], grid_copy[r][c] + 1)
                my_set.add((r - 1, c))
                q.append([r - 1, c])
            if (r + 1, c) not in my_set and r + 1 < self.rows and grid[r + 1][c] == 0:
                grid_copy[r + 1][c] = min(grid_copy[r + 1][c], grid_copy[r][c] + 1)
                my_set.add((r + 1, c))
                q.append([r + 1, c])
            if (r, c - 1) not in my_set and c - 1 >= 0 and grid[r][c - 1] == 0:
                grid_copy[r][c - 1] = min(grid_copy[r][c - 1], grid_copy[r][c] + 1)
                my_set.add((r, c - 1))
                q.append([r, c - 1])
            if (r, c + 1) not in my_set and c + 1 < self.cols and grid[r][c + 1] == 0:
                grid_copy[r][c + 1] = min(grid_copy[r][c + 1], grid_copy[r][c] + 1)
                my_set.add((r, c + 1))
                q.append([r, c + 1])

        return grid_copy


if __name__ == '__main__':
    f = FindSafestPathInGrid()
    print(f.maximumSafenessFactor([[1, 0, 0], [0, 0, 0], [0, 0, 1]]))

    f = FindSafestPathInGrid()
    print(f.maximumSafenessFactor([[0, 0, 1], [0, 0, 0], [0, 0, 0]]))

    f = FindSafestPathInGrid()
    print(f.maximumSafenessFactor([[0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0]]))
