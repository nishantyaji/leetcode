# Problem 1219


from typing import List


class PathWithMaxGold:

    def __init__(self):
        self.grid = [[]]
        self.rows = 0
        self.cols = 0

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.rows, self.cols = len(grid), len(grid[0])
        max_path = 0
        for r in range(self.rows):
            for c in range(self.cols):
                if grid[r][c] > 0:
                    my_set = set()
                    my_set.add(16 * r + c)
                    this_path = self.getMaxForStart(r, c, my_set, grid[r][c])
                    max_path = max(max_path, this_path)
        return max_path

    def getMaxForStart(self, r: int, c: int, my_set: set, running: int) -> int:
        max_path = 0

        count = 0
        if r > 0 and self.grid[r - 1][c] > 0 and (16 * (r - 1) + c) not in my_set:
            this_set = set(my_set)
            this_set.add(16 * (r - 1) + c)
            max_path = max(max_path, self.getMaxForStart(r - 1, c, this_set, running + self.grid[r - 1][c]))
            count += 1
        if r < self.rows - 1 and self.grid[r + 1][c] > 0 and (16 * (r + 1) + c) not in my_set:
            this_set = set(my_set)
            this_set.add(16 * (r + 1) + c)
            max_path = max(max_path, self.getMaxForStart(r + 1, c, this_set, running + self.grid[r + 1][c]))
            count += 1
        if c > 0 and self.grid[r][c - 1] > 0 and (16 * r + c - 1) not in my_set:
            this_set = set(my_set)
            this_set.add(16 * r + c - 1)
            max_path = max(max_path, self.getMaxForStart(r, c - 1, this_set, running + self.grid[r][c - 1]))
            count += 1
        if c < self.cols - 1 and self.grid[r][c + 1] > 0 and (16 * r + c + 1) not in my_set:
            this_set = set(my_set)
            this_set.add(16 * r + c + 1)
            max_path = max(max_path, self.getMaxForStart(r, c + 1, this_set, running + self.grid[r][c + 1]))
            count += 1

        if count == 0:
            max_path = running
        return max_path


if __name__ == '__main__':
    p = PathWithMaxGold()
    print(p.getMaximumGold([[0, 6, 0], [5, 8, 7], [0, 9, 0]]))
    # 24
    print(p.getMaximumGold([[1, 0, 7], [2, 0, 6], [3, 4, 5], [0, 3, 0], [9, 0, 20]]))
    # 28
