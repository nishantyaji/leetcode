# Problem 2134

from typing import List


class MinSwapsToGroupAll1sTogetherII:
    def minSwaps(self, nums: List[int]) -> int:
        ones = sum(nums)
        if ones <= 1:
            return 0

        def sum_1(s: int, j: int):
            if j >= s:
                return sum(nums[s:j + 1])
            else:
                nums2 = nums + nums
                return sum(nums2[s:(j + len(nums)) + 1])

        res = tem = ones - sum_1(0, (0 + ones - 1) % len(nums))
        for i in range(1, len(nums)):
            # sliding window of size "ones"
            tem = tem + (1 if nums[i - 1] == 1 else 0) - (1 if nums[(i + ones - 1) % len(nums)] == 1 else 0)
            if tem < res:
                res = tem
        return res


if __name__ == '__main__':
    m = MinSwapsToGroupAll1sTogetherII()
    print(m.minSwaps([0, 1, 0, 1, 1, 0, 0]))
    # 1
    print(m.minSwaps([0, 1, 0, 0, 1, 0, 0, 0, 1]))
    # 1
    print(m.minSwaps([0, 1, 1, 1, 0, 0, 1, 1, 0]))
    # 2
    print(m.minSwaps([1, 1, 0, 0, 1]))
    # 0
