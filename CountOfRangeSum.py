# Problem 327
import itertools
from typing import List


class CountOfRangeSum:

    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        result = 0
        # The following is an in efficient way even though we cache
        # bit_length = max(all_sum, all_sum + upper) + 1
        # fenwick = BIT(bit_length)
        # for idx, n in enumerate(nums):
        #     fenwick.update(idx + 1, n)
        # for i in range(1, len(nums) + 1):
        #     for j in range(1, i + 1):
        #         window_nums = fenwick.query(i) - fenwick.query(j - 1)
        #         result += (1 if lower <= window_nums <= upper else 0)

        # Rather use this loop (copied from others)
        # since
        # lower <= cum_sum(till b) - cum_sum(till a) <= upper
        # lower - cum_sum(till b) <= -cum_sum(till a) <= upper - cum_sum(till b)
        # cum_sum(till b) - lower >= cum_sum(till a) >= cum_sum(till b) - upper
        # Since a < b
        # the cum_sum(till a) should appear in the b's loop when we calculate
        # fenwick.query(cum_sum(tillb) - lower) - fenwick.query(cum_sum(tillb) - lower)
        # Similarly all such 'a's that fit the criteria with the other cum_sum being for b are calculated here
        prefix_sums = [0] + list(itertools.accumulate(nums))
        values = prefix_sums + [n - lower for n in prefix_sums] + [n - upper for n in prefix_sums]
        # Coordinate compression below
        compressed_map = {num: index + 1 for index, num in enumerate(sorted(set(values)))}
        fenwick = BIT(len(compressed_map))
        # We add 0 (1st element in prefix sum) to the fenwick tree
        # because apparently empty prefix sum is also counted
        # S(i, j) where i <= j
        for cum_sum in prefix_sums:
            result += (fenwick.query(compressed_map[cum_sum - lower]) - fenwick.query(
                compressed_map[cum_sum - upper] - 1))
            fenwick.update(compressed_map[cum_sum], 1)
        return result


class BIT:

    def __init__(self, size: int):
        self.size = size
        self.bit = [0] * (size + 1)

    def update(self, place: int, val: int):
        while place <= self.size:
            self.bit[place] += val
            place += (place & -place)

    def query(self, place: int):
        # Never ever @functools.cache this method. EVER
        result = 0
        while place > 0:
            result += self.bit[place]
            place -= (place & -place)
        return result


if __name__ == '__main__':
    c = CountOfRangeSum()
    print(c.countRangeSum([2147483647, -2147483648, -1, 0], -1, 0))
    print(c.countRangeSum([-2, 5, -1], -2, 2))
    # 3

    print(c.countRangeSum([0], 0, 0))
    # 1
    print(c.countRangeSum([-1, 1], 0, 0))
    # 1
