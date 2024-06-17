from typing import List


class CountPairsFormCompleteDayII:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        return sum([1 for i in range(len(hours)) for j in range(i + 1, len(hours)) if (hours[i] + hours[j]) % 24 == 0])


if __name__ == '__main__':
    w = CountPairsFormCompleteDayII()
