# Problem 1649
from typing import List


class BIT:
    def __init__(self, size: int):
        self.size = size
        self.bit = [0] * (size + 1)

    def update(self, place: int, val: int):
        while place <= self.size:
            self.bit[place] += val
            place += (place & -place)

    def query(self, place: int) -> int:
        result = 0
        while place > 0:
            result += self.bit[place]
            place -= (place & -place)
        return result

    def query_range(self, low: int, high: int):
        return self.query(high) - self.query(low - 1)


class CreateSortedArrayThroughInstructions:

    def createSortedArray(self, instructions: List[int]) -> int:
        res, mod_base = 0, 1000000007
        mp = {x: i + 1 for i, x in enumerate(sorted(set(instructions)))}
        limit = len(instructions) + 2

        fw = BIT(limit)

        for i, n in enumerate(instructions):
            before = fw.query(mp[n] - 1)
            after = fw.query_range(mp[n] + 1, limit)
            res = (res + min(before, after)) % mod_base
            fw.update(mp[n], 1)

        return res % mod_base


if __name__ == '__main__':
    c = CreateSortedArrayThroughInstructions()
    print(c.createSortedArray([1, 5, 6, 2]))
    print(c.createSortedArray([1, 2, 3, 6, 5, 4]))
    print(c.createSortedArray([1, 3, 3, 3, 2, 4, 2, 1, 2]))
