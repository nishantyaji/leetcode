# Problem 539
from typing import List


class MinTimeDiff:
    def findMinDifference(self, timePoints: List[str]) -> int:

        def min_time(s1: str, s2: str):
            [h1, s1] = list(map(int, s1.split(":")))
            [h2, s2] = list(map(int, s2.split(":")))
            if h1 == h2:
                return abs(s1 - s2)
            else:
                if h1 > h2:
                    h1mins = 60 * h1 + s1
                    h2amins = 60 * h2 + s2
                    h2bmins = 60 * (24 + h2) + s2
                    return min(abs(h2bmins - h1mins), abs(h2amins - h1mins))
                else:
                    h2mins = 60 * h2 + s2
                    h1amins = 60 * h1 + s1
                    h1bmins = 60 * (24 + h1) + s1
                    return min(abs(h1bmins - h2mins), abs(h1amins - h2mins))

        def sortFn(s):
            [hh, ss] = list(map(int, s.split(":")))
            return 60 * hh + ss

        timePoints.sort(key=sortFn)
        return min(
            [abs(min_time(timePoints[i], timePoints[(i + 1) % len(timePoints)])) for i in range(len(timePoints))])


if __name__ == '__main__':
    m = MinTimeDiff()
    print(m.findMinDifference(["23:59", "00:00"]))
    print(m.findMinDifference(["00:00", "23:59", "00:00"]))
    print(m.findMinDifference(["06:22", "10:48", "06:27", "05:46", "17:24"]))
