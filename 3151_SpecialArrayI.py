# 3151. Special Array I

from typing import List


class SpecialArrayI:

    def isArraySpecial(self, nums: List[int]) -> bool:
        for i in range(len(nums) - 1):
            if (nums[i] ^ nums[i+1]) & 1 == 0:
                return False
        return True

    def isArraySpecialSlow(self, nums: List[int]) -> bool:
        for i in range(len(nums) - 1):
            if (nums[i] - nums[i + 1]) % 2 == 0:
                return False
        return True


if __name__ == '__main__':
    w = SpecialArrayI()
