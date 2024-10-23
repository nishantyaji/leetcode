# Problem 749
import collections
import operator
from typing import List


class ContainVirus:

    def neis(self, t: tuple, nam: int, grid: List[List[int]], visited: set) -> list[tuple]:
        res, rows, cols = [], len(grid), len(grid[0])
        x, y = t
        if x < rows - 1:
            res.append((x + 1, y))
        if x > 0:
            res.append((x - 1, y))
        if y < cols - 1:
            res.append((x, y + 1))
        if y > 0:
            res.append((x, y - 1))
        return [nr for nr in res if nr not in visited and grid[nr[0]][nr[1]] == nam]

    def containVirus(self, isInfected: List[List[int]]) -> int:
        rows, cols, name, res = len(isInfected), len(isInfected[0]), 2, 0

        while True:
            visited = set()
            for r in range(rows):
                for c in range(cols):
                    if isInfected[r][c] == 1:
                        q = [(r, c)]
                        visited.add((r, c))
                        name += 1
                        while q:
                            rx, cx = q.pop()
                            visited.add((rx, cx))
                            isInfected[rx][cx] = name
                            nei = self.neis((rx, cx), 1, isInfected, visited)
                            for nei_ in nei:
                                visited.add(nei_)
                                # add the ones going to queue in visited,
                                # so that the queue does not have same cell twice
                            q = nei + q
            wall_map = collections.defaultdict(int)
            affected = collections.defaultdict(set)
            for r in range(rows):
                for c in range(cols):
                    if r - 1 >= 0 and isInfected[r - 1][c] == 0 and isInfected[r][c] > 0:
                        wall_map[isInfected[r][c]] += 1
                        affected[isInfected[r][c]].add((r - 1, c))
                    if r - 1 >= 0 and isInfected[r - 1][c] > 0 and isInfected[r][c] == 0:
                        wall_map[isInfected[r - 1][c]] += 1
                        affected[isInfected[r - 1][c]].add((r, c))
                    if c - 1 >= 0 and isInfected[r][c - 1] == 0 and isInfected[r][c] > 0:
                        wall_map[isInfected[r][c]] += 1
                        affected[isInfected[r][c]].add((r, c - 1))
                    if c - 1 >= 0 and isInfected[r][c - 1] > 0 and isInfected[r][c] == 0:
                        wall_map[isInfected[r][c - 1]] += 1
                        affected[isInfected[r][c - 1]].add((r, c))

            if not wall_map:
                break

            to_wall = sorted([(k, len(v)) for k, v in affected.items()], key=operator.itemgetter(1), reverse=True)[0]
            if not to_wall or to_wall[1] == 0:
                break
            res += wall_map[to_wall[0]]
            expanded = False
            for rex in range(rows):
                for cex in range(cols):
                    if isInfected[rex][cex] == to_wall[0]:
                        isInfected[rex][cex] = -to_wall[0]
                    elif 100000 > isInfected[rex][cex] > 0:
                        # expand
                        temp = self.neis((rex, cex), 0, isInfected, set())
                        for tem in temp:
                            isInfected[tem[0]][tem[1]] = 100000 + (isInfected[rex][cex] % 100000)
                            expanded = True

            # expand

            for rex in range(rows):
                for cex in range(cols):
                    if 100000 > isInfected[rex][cex] > 0:
                        temp = self.neis((rex, cex), 0, isInfected, set())
                        for tem in temp:
                            # Instead of 100000 we could use visited set here again
                            isInfected[tem[0]][tem[1]] = 100000 + (isInfected[rex][cex] % 100000)
                            expanded = True

            # make this grid an array of 1s and 0s (and frozen elements in negative)
            for rex in range(rows):
                for cex in range(cols):
                    if isInfected[rex][cex] > 100000:
                        isInfected[rex][cex] -= 100000
                    if isInfected[rex][cex] > 0:
                        isInfected[rex][cex] = 1
            if not expanded:
                break

        return res


if __name__ == '__main__':
    c = ContainVirus()

    print(c.containVirus([[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0],[1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,1,0,0],[0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],[0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0],[0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],[0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1],[0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,1,0,0],[0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0],[1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0]]))

    print(c.containVirus(
        [[0, 1, 0, 1, 1, 1, 1, 1, 1, 0],
         [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 1, 1, 1, 0, 0, 0, 1, 0],
         [0, 0, 0, 1, 1, 0, 0, 1, 1, 0],
         [0, 1, 0, 0, 1, 0, 1, 1, 0, 1],
         [0, 0, 0, 1, 0, 1, 0, 1, 1, 1],
         [0, 1, 0, 0, 1, 0, 0, 1, 1, 0],
         [0, 1, 0, 1, 0, 0, 0, 1, 1, 0],
         [0, 1, 1, 0, 0, 1, 1, 0, 0, 1],
         [1, 0, 1, 1, 0, 1, 0, 1, 0, 1]]

    ))  # 38
    print(c.containVirus(
        [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    ))  # 56
    
    print(c.containVirus([[1, 1, 1, 0, 0, 0, 0, 0, 0], [1, 0, 1, 0, 1, 1, 1, 1, 1], [1, 1, 1, 0, 0, 0, 0, 0, 0]]))  # 13
    print(c.containVirus(
        [[0, 1, 0, 0, 0, 0, 0, 1], [0, 1, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0]]))  # 10
    print(c.containVirus([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))  # 4
