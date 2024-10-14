# Problem 1643
import math
from typing import List


class KthSmallestInstruction:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        running = self.recurse(destination[0], destination[1], k)
        return "".join(running)

    def recurse(self, r: int, c: int, k: int):
        if c == 0:
            return ["V"] * r
        elif r == 0:
            return ["H"] * c
        limit = math.comb(r + c - 1, c - 1)
        # after the limit, the leading letter will be "V"
        if k > limit:
            return ["V"] + self.recurse(r - 1, c, k - limit)
        else:
            return ["H"] + self.recurse(r, c - 1, k)


if __name__ == '__main__':
    k = KthSmallestInstruction()
    print(k.kthSmallestPath([15, 2], 136))  # "VVVVVVVVVVVVVVVHH"
    print(k.kthSmallestPath([2, 3], 1))
    print(k.kthSmallestPath([2, 3], 2))
    print(k.kthSmallestPath([2, 3], 3))
