# Problem 1267

import collections
from typing import List


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        cntrr = collections.defaultdict(int)
        cntrc = collections.defaultdict(int)
        rows, cols = len(grid), len(grid[0])
        total = 0
        q = []
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    total += 1
                    cntrr[r] += 1
                    cntrc[c] += 1
                    q.append((r, c))

        for s in q:
            if cntrr[s[0]] == 1 and cntrc[s[1]] == 1:
                total -= 1
        return total
