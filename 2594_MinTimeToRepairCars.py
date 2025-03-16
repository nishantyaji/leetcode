# Problem 2594
import math
import sys
from typing import List


class MinTimeToRepairCars:
    def repairCars(self, ranks: List[int], cars: int) -> int:

        def check_possible(limit: int):
            total = cars
            for r in ranks:
                num = int(math.sqrt(limit / r))
                total -= num
            if total > 0:
                return False
            return True

        res, s, e = sys.maxsize, 0, ranks[-1] * cars * cars
        while s <= e:
            mid = (s + e) // 2
            flag = check_possible(mid)
            if flag:
                res = min(res, mid)
                e = mid - 1
            else:
                s = mid + 1
        return res


if __name__ == '__main__':
    m = MinTimeToRepairCars()
    print(m.repairCars([4, 2, 3, 1], 10))  # 16
    print(m.repairCars([5, 1, 8], 6))  # 16
