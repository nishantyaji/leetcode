import collections
from typing import List


class CountPairsFormCompleteDayII:

    def countCompleteDayPairs(self, hours: List[int]) -> int:
        my_dict = collections.defaultdict(int)
        result = 0
        for n in hours:
            n = n % 24
            if (24 - n) % 24 in my_dict:
                result += my_dict[(24 - n) % 24]
            my_dict[n] += 1
        return result


if __name__ == '__main__':
    w = CountPairsFormCompleteDayII()
    print(w.countCompleteDayPairs([12, 12, 30, 24, 24]))
    print(w.countCompleteDayPairs([72, 48, 24, 3]))
