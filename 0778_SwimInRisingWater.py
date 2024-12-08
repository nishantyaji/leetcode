# Problem 778
from typing import List


class SwimInRisingWater:

    def swimInWater(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        mx = -1
        for r in range(rows):
            for c in range(cols):
                mx = max(mx, grid[r][c])

        s, e, res = 0, mx, mx
        while s <= e:
            mid = (s + e) // 2
            flag = self.bfs(grid, mid)
            if flag:
                res = mid
                e = mid - 1
            else:
                s = mid + 1

        return res

    def bfs(self, grid: List[List[int]], depth: int) -> bool:
        rows, cols = len(grid), len(grid[0])
        if grid[0][0] > depth:
            return False

        q = [(0, 0)]
        visited = {(0, 0)}

        def get_neis(rr, cc):
            neis = []
            if rr > 0 and (rr - 1, cc) not in visited and grid[r - 1][c] <= depth:
                neis.append((rr - 1, cc))
            if rr < rows - 1 and (rr + 1, cc) not in visited and grid[r + 1][c] <= depth:
                neis.append((rr + 1, cc))
            if cc > 0 and (rr, cc - 1) not in visited and grid[r][c - 1] <= depth:
                neis.append((rr, cc - 1))
            if cc < cols - 1 and (rr, cc + 1) not in visited and grid[r][c + 1] <= depth:
                neis.append((rr, cc + 1))
            return neis

        while q:
            (r, c) = q.pop()
            if (r, c) == (rows - 1, cols - 1):
                return True
            neis = get_neis(r, c)
            visited.update(neis)
            q = neis + q

        return False


if __name__ == '__main__':
    s = SwimInRisingWater()
    print(s.swimInWater([[0, 2], [1, 3]]))
    print(s.swimInWater(
        [[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]]))
