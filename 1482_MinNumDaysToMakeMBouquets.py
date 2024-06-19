from typing import List


class MinNumDaysToMakeMBouquets:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        # m bouquets, k adjacent flowers
        if len(bloomDay) < m * k:
            return -1

        low, high = min(bloomDay), max(bloomDay)
        my_dict = {high: True}
        while low <= high:
            mid = (low + high) // 2
            if self.check_cdn(bloomDay, mid, m, k):
                my_dict[mid] = True
                high = mid - 1
            else:
                low = mid + 1

        return min(my_dict.keys())

    def check_cdn(self, bloomDay: List[int], day: int, m: int, k: int) -> bool:
        block, result = 0, 0
        for b in bloomDay:
            if b <= day:
                block += 1
            else:
                result += block // k
                block = 0
        result += block // k
        return result >= m


if __name__ == '__main__':
    m = MinNumDaysToMakeMBouquets()
    print(m.minDays([1, 10, 3, 10, 2], 3, 1))
    print(m.minDays([1, 10, 3, 10, 2], 3, 2))
    print(m.minDays([7, 7, 7, 7, 12, 7, 7], 2, 3))
