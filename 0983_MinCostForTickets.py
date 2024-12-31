# Problem 983
import functools
from typing import List


class MinCostForTickets:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # Count all 365 days (or superfluous days)
        # Dealing with just the days list will make the solution convoluted
        @functools.cache
        def find_fn(numm: int) -> int:
            if numm > days[-1]:
                return 0
            if numm not in days:
                return find_fn(numm+1)
            return min(find_fn(numm + 1) + costs[0], find_fn(numm + 7) + costs[1], find_fn(numm + 30) + costs[2])

        return find_fn(days[0])


if __name__ == '__main__':
    m = MinCostForTickets()
    print(m.mincostTickets([1, 4, 6, 7, 8, 20], [2, 7, 15]))  # 11
    print(m.mincostTickets([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2, 7, 15]))  # 17
