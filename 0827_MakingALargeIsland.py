# Problem 827
import collections
from typing import List


class MakingALargeIsland:
    def largestIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        cnt = 1

        def get_neis(rr, cc):
            neis, others = [], []
            if rr > 0:
                if grid[rr - 1][cc] == 1:
                    neis.append((rr - 1, cc))
                elif grid[rr - 1][cc] == 0:
                    others.append((rr - 1, cc))
            if rr < rows - 1:
                if grid[rr + 1][cc] == 1:
                    neis.append((rr + 1, cc))
                elif grid[rr + 1][cc] == 0:
                    others.append((rr + 1, cc))
            if cc > 0:
                if grid[rr][cc - 1] == 1:
                    neis.append((rr, cc - 1))
                elif grid[rr][cc - 1] == 0:
                    others.append((rr, cc - 1))
            if cc < cols - 1:
                if grid[rr][cc + 1] == 1:
                    neis.append((rr, cc + 1))
                elif grid[rr][cc + 1] == 0:
                    others.append((rr, cc + 1))
            return [neis, others]

        borders = collections.defaultdict(set)
        count_map = collections.defaultdict(int)
        mx = 1
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    cnt += 1
                    q = [(i, j)]
                    while q:
                        x, y = q.pop()
                        if grid[x][y] == 1:
                            grid[x][y] = cnt
                            count_map[cnt] += 1
                            mx = max(mx, count_map[cnt])
                            neigs, oth = get_neis(x, y)
                            for o in oth:
                                borders[o].add(cnt)
                            q = neigs + q

        for k, v in borders.items():
            sm = sum(count_map[x] for x in v) + 1
            mx = max(sm, mx)
        return mx
