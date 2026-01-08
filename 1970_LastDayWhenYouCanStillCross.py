# Prblem 1970
from typing import List


class LastDayWhenYouCanStillCross:

    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        cells = [(x[0] - 1, x[1] - 1) for x in cells]
        s, e = 1, len(cells)

        mp = {}
        while s <= e:
            m = (s + e) // 2
            c = self.check(row, col, set(cells[:m]))
            if c:
                mp[m] = c
                s = m + 1
            else:
                e = m - 1

        return max(mp.keys())

    def check(self, row: int, col: int, cells: set):
        visited = set(cells)
        q = [(0, i) for i in range(col) if (0, i) not in visited]

        def get_neighbours(x: int, y: int):
            neis_list = []
            if x > 0 and (x - 1, y) not in visited:
                neis_list.append((x - 1, y))
            if x < row - 1 and (x + 1, y) not in visited:
                neis_list.append((x + 1, y))
            if y > 0 and (x, y - 1) not in visited:
                neis_list.append((x, y - 1))
            if y < col - 1 and (x, y + 1) not in visited:
                neis_list.append((x, y + 1))
            return neis_list

        while q:
            node = q.pop()
            if node[0] == row - 1:
                return True
            neis = get_neighbours(node[0], node[1])
            visited.update(set(neis))
            q = neis + q
        return False


if __name__ == '__main__':
    l = LastDayWhenYouCanStillCross()
    print(l.latestDayToCross(2, 2, [[1,1],[2,1],[1,2],[2,2]]))
    print(l.latestDayToCross(2, 2, [[1,1],[1,2],[2,1],[2,2]]))
    print(l.latestDayToCross(3, 3, [[1,2],[2,1],[3,3],[2,2],[1,1],[1,3],[2,3],[3,2],[3,1]]))