# Problem 1791
from typing import List


class FindCenterOfStarGraph:
    def findCenter(self, edges: List[List[int]]) -> int:
        this_set = set(edges[0])
        return edges[1][1] if edges[1][1] in this_set else edges[1][0]
