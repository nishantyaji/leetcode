# Problem 493

from typing import List


class ReversePairs:
    def reversePairs(self, nums: List[int]) -> int:
        values = nums + [2 * n for n in nums]
        result, max_val = 0, max(values)
        # Use coordinate compression to avoid TLE and MLE
        compressed_map = {num: index + 1 for index, num in enumerate(sorted(set(values)))}
        fenwick = BIT(len(compressed_map))

        # Using Fenwick tree or Binary Indexed Tree
        # Since we are counting elements which are >= twice to any of the right elements
        # we take the range query from twice element to max
        # Also we are querying whether any answer elements are in that range for this element
        # the answer elements would precede this element
        for elem in nums:
            result += fenwick.query(compressed_map[max_val]) - fenwick.query(compressed_map[2 * elem])
            fenwick.update(compressed_map[elem], 1)
        return result


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


if __name__ == '__main__':
    r = ReversePairs()
    print(r.reversePairs([1, 3, 2, 3, 1]))
    print(r.reversePairs([2, 4, 3, 5, 1]))
    print(r.reversePairs([-5, -5]))
    print(r.reversePairs([2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647]))
