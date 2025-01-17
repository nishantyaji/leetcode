# Problem 3171
import collections
import functools
from typing import List


class FindSubArrayWithBitWiseAndClosestToK:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        # This code is all over the place
        # High cyclomatic complexity
        bin_nums = [self.get_bin_rep(n) for n in nums]
        total = collections.defaultdict(int)
        self.add_dict(total, bin_nums[0])
        abs_min_diff = abs(k - nums[0])
        i, j = 0, 0
        while i < len(nums) and j < len(nums):
            or_val = self.or_val_dict(total)
            if abs(k - or_val) < abs_min_diff:
                if i <= j:
                    abs_min_diff = abs(k - or_val)
                else:
                    j += 1
                    if j < len(nums):
                        self.add_dict(total, bin_nums[j])
                    continue
                if or_val >= k:
                    i += 1
                    self.rem_dict(total, bin_nums[i - 1])
            else:
                temp = abs(k - or_val)
                if temp < abs_min_diff:
                    abs_min_diff = temp

                if or_val >= k:
                    i += 1
                    self.rem_dict(total, bin_nums[i - 1])
                    if i > j and j < len(nums) - 1:
                        j += 1
                        self.add_dict(total, bin_nums[j])
                else:
                    j += 1
                    if j < len(nums):
                        self.add_dict(total, bin_nums[j])

        return abs_min_diff

    @functools.cache
    def get_bin_rep(self, num: int) -> List[int]:
        return [ord(ch) - ord('0') for ch in bin(num)[2:][::-1]]

    def value_arr(self, bins: List[int]) -> int:
        result, mul = 0, 1
        for b in bins:
            result += b * mul
            mul = mul << 1
        return result

    def add_dict(self, total: dict, num_arr: List[int]):
        for idx, n in enumerate(num_arr):
            if n == 1:
                total[idx] += 1

    def rem_dict(self, total: dict, num_arr: List[int]):
        for idx, n in enumerate(num_arr):
            if n == 1:
                total[idx] -= 1
            if total[idx] == 0:
                del total[idx]

    def or_val_dict(self, total: dict):
        if len(total) == 0:
            return 0
        max_pow, result = max(total.keys()), 0
        for i in range(0, max_pow + 1):
            if total[i] > 0:
                result += pow(2, i)
        return result


if __name__ == '__main__':
    f = FindSubArrayWithBitWiseAndClosestToK()
    print(f.minimumDifference([48, 49, 14, 43, 49], 5))
    print(f.minimumDifference([42, 49, 95, 76, 66], 12))  # 30
    print(f.minimumDifference([1, 10], 6))  # 4
    print(f.minimumDifference([2], 3))  # 1
    print(f.minimumDifference([1], 10))  # 9
    print(f.minimumDifference([1, 2, 4, 5], 3))  # 0
    print(f.minimumDifference([1, 2, 1, 2], 2))  # 0
    print(f.minimumDifference([1, 3, 1, 3], 2))  # 1
