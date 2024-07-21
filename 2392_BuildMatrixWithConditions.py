# Problem 2392
import collections
from typing import List


class BuildMatrixWithConditions:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        # Topological sort - BFS used here
        rmp, cmp = collections.defaultdict(list), collections.defaultdict(list)
        r_in, c_in = collections.defaultdict(int), collections.defaultdict(int)
        for [above, below] in rowConditions:
            rmp[below].append(above)
            r_in[above] += 1
        for [left, right] in colConditions:
            cmp[right].append(left)
            c_in[left] += 1

        r_order, c_order, r_in_0, c_in_0 = [], [], [], []
        for i in range(1, k + 1):
            if i not in r_in:
                r_in_0.append(i)
            if i not in c_in:
                c_in_0.append(i)
        r_order, c_order = r_order + r_in_0, c_order + c_in_0

        flag = False
        while len(r_in) > 0:
            if flag:
                r_in_0 = [k for k, v in r_in.items() if v == 0]
                if len(r_in_0) == 0:
                    return []
                r_order = r_order + r_in_0
                for r_0 in r_in_0:
                    del r_in[r_0]
            for r in r_in_0:
                for r_ab in rmp[r]:
                    r_in[r_ab] -= 1
            flag = True

        flag = False
        while len(c_in) > 0:
            if flag:
                c_in_0 = [k for k, v in c_in.items() if v == 0]
                if len(c_in_0) == 0:
                    return []
                c_order = c_order + c_in_0
                for c_0 in c_in_0:
                    del c_in[c_0]
            for c in c_in_0:
                for c_ab in cmp[c]:
                    c_in[c_ab] -= 1
            flag = True

        grid = [[0 for c in range(k)] for r in range(k)]
        for n in range(1, k + 1):
            r_idx = k - 1 - [i for i, x in enumerate(r_order) if x == n][0]
            c_idx = k - 1 - [i for i, x in enumerate(c_order) if x == n][0]
            grid[r_idx][c_idx] = n

        return grid


if __name__ == '__main__':
    b = BuildMatrixWithConditions()
    print(b.buildMatrix(3, [[1, 2], [3, 2]], [[2, 1], [3, 2]]))
    # [[3,0,0],[0,0,1],[0,2,0]]
    print()
    print(b.buildMatrix(3, [[1, 2], [2, 3], [3, 1], [2, 3]], [[2, 1]]))
    # []
