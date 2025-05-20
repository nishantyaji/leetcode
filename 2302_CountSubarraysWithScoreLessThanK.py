from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:

        window, res = [], 0
        left, right, total, count = 0, 0, 0, 0

        while right < len(nums):
            count, total = count + 1, total + nums[right]
            if total * count >= k:
                while count * total >= k and left <= right:
                    res += len(nums) - right
                    left += 1
                    count -= 1
                    total -= nums[left - 1]
            right += 1
        self.calc(nums, k)
        return (len(nums) * (len(nums) + 1)) // 2 - res


if __name__ == '__main__':
    s = Solution()
    print(s.countSubarrays([9, 5, 3, 8, 4, 7, 2, 7, 4, 5, 4, 9, 1, 4, 8, 10, 8, 10, 4, 7], 4))  # 3
    print(s.countSubarrays([2, 1, 4, 3, 5], 10))
    print(s.countSubarrays([1, 1, 1], 5))
