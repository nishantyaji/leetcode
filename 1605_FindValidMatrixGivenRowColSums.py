# Problem 1605
import operator
from typing import List


class FindValidMatrixGivenRowColSums:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        # This problem needs trimming, big time !
        rows, cols = len(rowSum), len(colSum)
        places = [rows * cols]
        grid = [[-1 for c in range(cols)] for r in range(rows)]
        r_tup = [[r, i] for i, r in enumerate(rowSum)]
        c_tup = [[c, i] for i, c in enumerate(colSum)]

        while places[0] > 0 and (len(r_tup) > 0 or len(c_tup) > 0):
            self.recurse(grid, r_tup, c_tup, places)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == -1:
                    grid[r][c] = 0
        return grid

    def trim(self, r_tup: List[List[int]], c_tup: List[List[int]], places: List[int]):
        i = 0
        while len(r_tup) > 0 and i < len(r_tup) and r_tup[i][0] == 0:
            i += 1
        while i > 0:
            r_tup.pop(0)
            i -= 1
            places[0] -= 1
        i = 0
        while len(c_tup) > 0 and i < len(c_tup) and c_tup[i][0] == 0:
            i += 1
        while i > 0:
            c_tup.pop(0)
            i -= 1
            places[0] -= 1

    def recurse(self, grid: List[List[int]], r_tup: List[List[int]], c_tup: List[List[int]], places: List[int]):
        self.trim(r_tup, c_tup, places)
        if places[0] > 0 and (len(r_tup) > 0 or len(c_tup) > 0):
            print(places[0])
            r_tup.sort(key=operator.itemgetter(0))
            c_tup.sort(key=operator.itemgetter(0))

            if len(c_tup) > 0 and (len(r_tup) == 0 or c_tup[0][0] < r_tup[0][0]):
                min_c_idx = c_tup[0][1]
                rs = list(map(lambda x: x[1], r_tup))
                for idx, r in enumerate(rs):
                    if grid[r][min_c_idx] == -1:
                        grid[r][min_c_idx] = c_tup[0][0]
                        places[0] -= 1
                        r_tup[idx][0] = r_tup[idx][0] - c_tup[0][0]
                        c_tup.pop(0)
                        break
                return
            else:
                min_r_idx = r_tup[0][1]
                cs = list(map(lambda x: x[1], c_tup))
                for idx, c in enumerate(cs):
                    if grid[min_r_idx][c] == -1:
                        grid[min_r_idx][c] = r_tup[0][0]
                        places[0] -= 1
                        c_tup[idx][0] = c_tup[idx][0] - r_tup[0][0]
                        r_tup.pop(0)
                        break
                return


if __name__ == '__main__':
    f = FindValidMatrixGivenRowColSums()
    print(f.restoreMatrix([3, 8], [4, 7]))
    print(f.restoreMatrix([5, 7, 10], [8, 6, 8]))
