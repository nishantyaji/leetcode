# Problem 1266
from typing import List


class MinTimeVisitingAllPoints:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res = 0
        ref = points[0]
        for i in range(1, len(points)):
            res += self.distance(ref, points[i])
            ref = points[i]
        return res

    def distance(self, point1, point2):
        x = abs(point1[0] - point2[0])
        y = abs(point1[1] - point2[1])
        return max(x, y)
