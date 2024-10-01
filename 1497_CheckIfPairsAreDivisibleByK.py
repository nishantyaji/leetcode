# Problem 1497
import collections
from typing import List


class CheckIfPairsAreDivisibleByK:
    def canArrange(self, arr: List[int], k: int) -> bool:
        self_inverse = [0] + ([k // 2] if k % 2 == 0 else [])
        cntr = collections.Counter([a % k for a in arr])
        return all(map(lambda x: cntr[x] % 2 == 0, self_inverse)) and all(
            [v == cntr[k - a] for a, v in cntr.items() if a not in self_inverse])


if __name__ == '__main__':
    c = CheckIfPairsAreDivisibleByK()
    print(c.canArrange([1, 2, 3, 4, 5, 10, 6, 7, 8, 9], 5))
