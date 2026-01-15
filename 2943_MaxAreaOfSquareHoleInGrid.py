# Problem 2943
from typing import List


class MaxAreaOfSquareHoleInGrid:

    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        hBars.sort()
        vBars.sort()
        # find continuous gap in the grid
        # by looking at the largest window with consecutive bars removed
        hmax = self.get_max(hBars, n)
        # do the same vertically
        vmax = self.get_max(vBars, m)
        # Largest square's side is the minimum of horizontal window, vertical window
        side = min(hmax, vmax)
        return side * side


    def get_max(self, arr: List[int], limit):
        prev, mx, cnt, s, e = -2, 0,1, 0, 0
        # if the bars are removed from the extremities then they do not contribute for
        # the window for square
        # Therefore we need to discount these "extremity" bars
        while arr[s] == s:
            s += 1
        arr = arr[s:]
        while arr[e] == limit + 2 + e:
            e -= 1
        if e < 0:
            arr = arr[:e]
        for h in arr:
            cnt = cnt + 1 if prev == h - 1 else 1
            prev = h
            mx = max(cnt, mx)
        return mx + 1

if __name__ == '__main__':
    m = MaxAreaOfSquareHoleInGrid()
    print(m.maximizeSquareHoleArea(2, 1, [2,3], [2]))
    print(m.maximizeSquareHoleArea(1, 1, [2], [2]))
    print(m.maximizeSquareHoleArea(2, 3, [2,3], [2,4]))