# Problem 2975
from typing import List


class MaxSquareAreaByRemovingFencesFromAField:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        hFences.append(1)
        hFences.append(m)
        vFences.append(1)
        vFences.append(n)
        hFences.sort()
        vFences.sort()
        h_set, v_set = set(), set()
        for i in range(len(hFences)):
            for j in range(i + 1, len(hFences)):
                h_set.add(hFences[j] - hFences[i])
        for i in range(len(vFences)):
            for j in range(i + 1, len(vFences)):
                v_set.add(vFences[j] - vFences[i])
        ixn = h_set.intersection(v_set)
        mx = 0 if not ixn else max(ixn)
        return (mx * mx) % 1000000007 if ixn else -1
