# Problem 3531
import bisect
import collections
from typing import List


class CountCoveredBuildings:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        for_rows = collections.defaultdict(list)
        for_cols = collections.defaultdict(list)

        for x, y in buildings:
            for_rows[x].append(y)
            for_cols[y].append(x)

        for x in for_rows:
            for_rows[x].sort()
        for y in for_cols:
            for_cols[y].sort()

        res = 0
        for x, y in buildings:
            y1 = bisect.bisect_left(for_rows[x], y)
            y2 = bisect.bisect_right(for_rows[x], y)
            x1 = bisect.bisect_left(for_cols[y], x)
            x2 = bisect.bisect_right(for_cols[y], x)
            if y1 > 0 and y2 < len(for_rows[x]) and x1 > 0 and x2 < len(for_cols[y]):
                res += 1
        return res
