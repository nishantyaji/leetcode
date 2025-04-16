# Problem 2537
from typing import List


class CountNumOfGoodSubArrays:

    def countGood(self, nums: List[int], k: int) -> int:
        def rem_(dd: dict, key):
            if key in dd:
                dd[key] -= 1
                if dd[key] == 0:
                    del dd[key]

        def add_(dd: dict, key):
            if key not in dd:
                dd[key] = 0
            dd[key] += 1

        left, right, run_count, total, window = 0, -1, 0, 0, {}
        while left < len(nums):

            while run_count >= k:
                total += (len(nums) - right)
                left += 1
                run_count -= (window[nums[left - 1]] - 1)
                rem_(window, nums[left - 1])
            if right < len(nums) - 1:
                right += 1
                add_(window, nums[right])
                run_count += (window[nums[right]] - 1)
            else:
                left += 1
                run_count -= (window[nums[left - 1]] - 1)
                rem_(window, nums[left - 1])
        return total


if __name__ == '__main__':
    c = CountNumOfGoodSubArrays()
    print(c.countGood([3, 1, 4, 3, 2, 2, 4], 2))  # 4
    print(c.countGood([1, 1, 1, 1, 1], 10))  # 1


