# Problem 2401
from typing import List


class LongestNiceArray:

    def longestNiceSubarray(self, nums: List[int]) -> int:
        def get_bits(nn: int) -> set:
            bin_rep = format(nn, "b")[::-1]
            return set([i1 for i1, x in enumerate(bin_rep) if x == "1"])

        sets = [get_bits(n) for n in nums]
        res = 1

        for i in range(len(nums)):
            temp = sets[i]
            for j in range(1, min(30, len(nums) - i)):
                if temp.intersection(sets[i + j]):
                    break
                else:
                    res = max(res, j + 1)
                    temp.update(sets[i + j])
        return res


if __name__ == '__main__':
    l = LongestNiceArray()
    print(l.longestNiceSubarray([1, 3, 8, 48, 10]))
    print(l.longestNiceSubarray([3, 1, 5, 11, 13]))
