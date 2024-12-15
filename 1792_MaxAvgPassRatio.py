# Problem 1792
import heapq
from typing import List


class MaxAvgPassRatio:

    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        pq = [(t[0] / t[1] - (t[0] + 1) / (t[1] + 1), t[0], t[1]) for t in classes]
        heapq.heapify(pq)

        for _ in range(extraStudents):
            (_, p, s) = heapq.heappop(pq)
            heapq.heappush(pq, ((p + 1) / (s + 1) - (p + 2) / (s + 2), p + 1, s + 1))

        res = 0
        while pq:
            (_, p, s) = heapq.heappop(pq)
            res += (p / s)

        return res / len(classes)


if __name__ == '__main__':
    m = MaxAvgPassRatio()
    print(m.maxAverageRatio([[1, 2], [3, 5], [2, 2]], 2))
    print(m.maxAverageRatio([[2, 4], [3, 9], [4, 5], [2, 10]], 4))
