# Problem 1905

from typing import List


class CountSubIslands:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        isle = 1
        rows, cols = len(grid2), len(grid2[0])

        def get_neighbours(r: int, c: int, visited: int):
            neighbours = []
            if r > 0 and grid2[r - 1][c] == isle:
                grid2[r - 1][c] = visited
                neighbours.append([r - 1, c])
            if c > 0 and grid2[r][c - 1] == isle:
                grid2[r][c - 1] = visited
                neighbours.append([r, c - 1])
            if r < rows - 1 and grid2[r + 1][c] == isle:
                grid2[r + 1][c] = visited
                neighbours.append([r + 1, c])
            if c < cols - 1 and grid2[r][c + 1] == isle:
                grid2[r][c + 1] = visited
                neighbours.append([r, c + 1])
            return neighbours

        isle_count = 0
        for row in range(0, rows):
            for col in range(0, cols):
                if grid2[row][col] == isle:
                    is_subset = True
                    eval_list = [[row, col]]
                    grid2[row][col] = isle_count + 2
                    while len(eval_list) > 0:
                        [temp_row, temp_col] = eval_list[0]
                        if grid1[temp_row][temp_col] != isle:
                            is_subset = False
                        del eval_list[0]
                        neighbours = get_neighbours(temp_row, temp_col, isle_count + 2)
                        eval_list = eval_list + neighbours
                    if is_subset:
                        isle_count += 1

        return isle_count


if __name__ == '__main__':
    c = CountSubIslands()
    print(c.countSubIslands([[1, 0, 1, 0, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [1, 0, 1, 0, 1]],
                            [[0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [0, 1, 0, 1, 0], [0, 1, 0, 1, 0], [1, 0, 0, 0, 1]]))
