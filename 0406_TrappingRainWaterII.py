# Problem 407
import heapq
from typing import List


class TrappingRainWaterII:

    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        # Optimize the flow.
        pq = []
        for i in range(1, len(heightMap) - 1):
            for j in range(1, len(heightMap[0]) - 1):
                heapq.heappush(pq, (heightMap[i][j], i, j))

        def get_neis(x, y, val, exclude):
            loops = [[-1, 0], [1, 0], [0, 1], [0, -1]]
            neis, bord = [], []
            for dx, dy in loops:
                new_x, new_y = x + dx, y + dy
                if 0 < new_x < len(heightMap) - 1 and 0 < new_y < len(heightMap[0]) - 1:
                    # non border
                    if heightMap[new_x][new_y] == val:
                        if (new_x, new_y) not in exclude:
                            neis.append((new_x, new_y))
                    else:
                        bord.append(heightMap[new_x][new_y])
                else:
                    if 0 <= new_x < len(heightMap) and 0 <= new_y < len(heightMap[0]):
                        bord.append(heightMap[new_x][new_y])
            return [neis, bord]

        res = 0
        while pq:
            val, x, y = heapq.heappop(pq)
            if val != heightMap[x][y]:
                continue
            q = [(x, y)]
            others = []
            count = 0
            visited = {(x, y)}
            while q:
                nodex, nodey = q.pop()
                visited.add((nodex, nodey))
                count += 1
                [neis, bord] = get_neis(nodex, nodey, val, visited)
                visited.update(neis)
                q = neis + q
                others += bord
            min_bord = min(others)
            if min_bord > val:
                res += (count * (min_bord - val))
                for (nodex, nodey) in visited:
                    heightMap[nodex][nodey] = min_bord
        return res


if __name__ == '__main__':
    t = TrappingRainWaterII()
    print(t.trapRainWater([[3, 3, 3, 3, 3], [3, 2, 2, 2, 3], [3, 2, 1, 2, 3], [3, 2, 2, 2, 3], [3, 3, 3, 3, 3]]))  # 10
    print(
        t.trapRainWater([[12, 13, 1, 12], [13, 4, 13, 12], [13, 8, 10, 12], [12, 13, 12, 12], [13, 13, 13, 13]]))  # 14
    print(t.trapRainWater([[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4], [2, 3, 3, 2, 3, 1]]))  # 4
