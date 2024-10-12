# Problem 2406
import heapq
from typing import List


class DivideIntervalsIntoMinNumGroups:

    def minGroups(self, intervals: List[List[int]]) -> int:

        # Better approach with line sweep in the editorial
        # Find out the maximum number of concurrent/overlapping intervals (at any point)
        # That should be the minimum Groups answer

        intervals.sort(key=lambda x: (10 ** 6) * x[0] + x[1])
        pq = []
        heapq.heapify(pq)
        for i in intervals:
            if not pq or pq[0][0] >= i[0]:
                new_group = (i[1], [i])
                heapq.heappush(pq, new_group)
                continue

            limit, group = heapq.heappop(pq)
            group.append(i)
            heapq.heappush(pq, (i[1], group))

        return len(pq)


if __name__ == '__main__':
    d = DivideIntervalsIntoMinNumGroups()
    print(d.minGroups([[5, 10], [6, 8], [1, 5], [2, 3], [1, 10]]))  # 3
    print(d.minGroups([[1, 3], [5, 6], [8, 10], [11, 13]]))  # 1
