import collections
import heapq
from typing import List


class MeeitngRoomsIII:

    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings = [(x[0], x[1]) for x in meetings]
        heapq.heapify(meetings)
        rooms = [x for x in range(n)]
        heapq.heapify(rooms)
        count = collections.defaultdict(int)
        ongoing = []
        while meetings:
            while ongoing and ongoing[0][0] <= meetings[0][0]:
                e, r, s = heapq.heappop(ongoing)
                heapq.heappush(rooms, r)

            ms, me = heapq.heappop(meetings)
            if rooms:
                mr = heapq.heappop(rooms)
                count[mr] += 1
                heapq.heappush(ongoing, (me, mr, ms))
            else:
                oe, orr, os = heapq.heappop(ongoing)
                # Since we are popping the top here
                # we should always have the following order in the tuple
                # first ending time and then room number
                # if there are more than room number that have the same ending time
                # then always pop the least room number first
                count[orr] += 1
                heapq.heappush(ongoing, (oe + me - ms, orr, oe))

        mx = max(count.values())
        res = min(r for r, c in count.items() if c == mx)
        return res

if __name__ == '__main__':
    m = MeeitngRoomsIII()
    print(m.mostBooked(2, [[0, 10], [1, 5], [2, 7], [3, 4]]))  # 0
    print(m.mostBooked(2, [[43,44],[34,36],[11,47],[1,8],[30,33],[45,48],[23,41],[29,30]])) # 1
    print(m.mostBooked(4, [[38, 44], [17, 38], [6, 29], [34, 40], [7, 14], [4, 27]])) # 0
    print(m.mostBooked(4, [[12, 44], [27, 37], [48, 49], [46, 49], [24, 44], [32, 38], [21, 49], [13, 30]]))  # 1
    print(m.mostBooked(4, [[19, 20], [14, 15], [13, 14], [11, 20]]))  # 1
    print(m.mostBooked(2, [[0, 10], [1, 2], [12, 14], [13, 15]]))  # 0
    print(m.mostBooked(4, [[18, 19], [3, 12], [17, 19], [2, 13], [7, 10]]))  # 0

    print(m.mostBooked(3, [[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]]))  # 1