# Problem 3169
from typing import List


class CountDaysWithoutMeetings:

    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings = [(m[0], m[1]) for m in meetings]
        meetings.sort(key=lambda x: (x[0], -x[1]))
        start, res = 0, 0
        for i, (s, e) in enumerate(meetings):
            if s > start:
                res += (s - start - 1)
            start = max(start, e)

        if start < days:
            res += (days - start)
        return res


if __name__ == '__main__':
    c = CountDaysWithoutMeetings()
    print(c.countDays(4, [[2, 3], [1, 2], [2, 3], [2, 4], [1, 2], [1, 3]]))   # 0
    print(c.countDays(8, [[3, 4], [4, 8], [2, 5], [3, 8]]))  # 1
    print(c.countDays(10, [[5, 7], [1, 3], [9, 10]]))  # 2
    print(c.countDays(5, [[2, 4], [1, 3]]))  # 1
    print(c.countDays(6, [[1, 6]]))  # 0
