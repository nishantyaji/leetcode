# Problem 2136
import heapq
from typing import List


class EarliestPossibleDayOfFullBloom:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        tuples = list(zip(plantTime, growTime))
        tuples.sort(key=lambda m: (-m[1], m[0]))

        run_p, run_g = 0, 0
        for t in tuples:
            run_p += t[0]
            run_g = max(run_g, run_p + t[1])
        return run_g

    def earliestFullBloom2(self, plantTime: List[int], growTime: List[int]) -> int:
        # note that Sum(plantTime) is anyways expended in planting
        # we need to overlap the growTime as much as possible
        # to ensure overlap (and no gaps between grows)
        # it is advisable to have the plants with higher growTime to come before
        # If the longer growTime plants are planted towards the end
        # then there will be more overshoot time after Sum(plantTime)
        tuples = list(zip(plantTime, growTime))
        pq = [(-m[1], m[0]) for m in tuples]
        heapq.heapify(pq)

        p_run, g_run = 0, 0
        while pq:
            gg, pp = heapq.heappop(pq)
            gg = -gg
            p_run += pp
            g_run = max(g_run, p_run + gg)

        return g_run


if __name__ == '__main__':
    e = EarliestPossibleDayOfFullBloom()
    print(e.earliestFullBloom([1, 4, 3], [2, 3, 1]))
    print(e.earliestFullBloom([1, 2, 3, 2], [2, 1, 2, 1]))
    print(e.earliestFullBloom([1], [1]))
