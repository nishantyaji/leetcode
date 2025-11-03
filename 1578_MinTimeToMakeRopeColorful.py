# Problem 1578
import heapq
from typing import List


class MinTimeToMakeRopeColorful:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        prev, pq, res = "-", [], 0
        for i, c in enumerate(colors):
            if c == prev:
                heapq.heappush(pq, -neededTime[i])
            else:
                if pq:
                    heapq.heappop(pq)
                    res += -1 * sum(pq)
                pq = []
                heapq.heappush(pq, -neededTime[i])
                prev = c

        if pq:
            heapq.heappop(pq)
            res += -1 * sum(pq)
        return res


if __name__ == '__main__':
    m = MinTimeToMakeRopeColorful()
    print(m.minCost("abaac", [1, 2, 3, 4, 5]))
    print(m.minCost("abc", [1, 2, 3]))
    print(m.minCost("aabaa", [1, 2, 3, 4, 1]))
    print(m.minCost("bbbaaa", [4, 9, 3, 8, 8, 9]))  # 23
