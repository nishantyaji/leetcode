# Probelm 219
from typing import List


class ContainsDuplicateII:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        my_dict = {}
        for i in range(0, min(k + 1, len(nums))):
            self.add_dict(my_dict, nums[i])

        if self.check(my_dict):
            return True

        for i in range(k + 1, len(nums)):
            self.remove_dict(my_dict, nums[i - k - 1])
            self.add_dict(my_dict, nums[i])
            if self.check_add(my_dict, nums[i]):
                return True
        return False

    def check(self, my_dict):
        values = [v for k, v in my_dict.items() if v > 1]
        return len(values) > 0

    def check_add(self, my_dict, num: int):
        return my_dict[num] > 1

    def add_dict(self, my_dict: dict, num: int):
        if num not in my_dict:
            my_dict[num] = 0
        my_dict[num] += 1

    def remove_dict(self, my_dict: dict, num: int):
        my_dict[num] = my_dict[num] - 1
        if my_dict[num] == 0:
            del my_dict[num]


if __name__ == '__main__':
    c = ContainsDuplicateII()
    print(c.containsNearbyDuplicate([1, 2, 3, 1], 3))
    print(c.containsNearbyDuplicate([1, 0, 1, 1], 1))
    print(c.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))
