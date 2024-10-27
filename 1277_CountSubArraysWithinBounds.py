# problem 2444

from typing import List

class CountSubArraysWithinBounds:

    @staticmethod
    def add_to_dict(mydict, num):
        if num not in mydict:
            mydict[num] = 1
        else:
            mydict[num] = mydict[num] + 1

    @staticmethod
    def remove_from_dict(mydict, num):
        if num in mydict:
            if mydict[num] == 1:
                del mydict[num]
            else:
                mydict[num] = mydict[num] - 1
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        result = 0
        left = 0
        my_dict = {}

        prev_min_occur = []
        prev_max_occur = []

        prev_min_idx = -1
        prev_max_idx = -1
        for idx in range(0, len(nums)):
            val = nums[idx]
            if val == minK:
                prev_min_idx = idx
            if val == maxK:
                prev_max_idx = idx
            prev_min_occur.append(prev_min_idx)
            prev_max_occur.append(prev_max_idx)



        for idx in range(0, len(nums)):
            if nums[idx] > maxK or nums[idx] < minK or idx == len(nums) - 1:
                keys = list(my_dict.keys())
                keys.sort()
                if keys[0] == minK and keys[-1] == maxK:
                    last_possible_subarray_end = max(prev_min_occur[idx], prev_max_occur[idx])
                    result += last_possible_subarray_end - left
                    while last_possible_subarray_end >= left:
                        last_possible_subarray_end -= 1
                        self.remove_from_dict(my_dict, nums[last_possible_subarray_end])
                        keys = list(my_dict.keys())
                        if len(keys) == 0:
                            break
                        keys.sort()
                        if keys[0] == minK and keys[-1] == maxK:
                            last_possible_subarray_end = max(prev_min_occur[last_possible_subarray_end], prev_max_occur[last_possible_subarray_end])
                            result += last_possible_subarray_end - left
                        else:
                            break
                    left = idx + 1
                    my_dict= {}
            else:
                self.add_to_dict(my_dict, nums[idx])

        return result


if __name__ == '__main__':
    s = CountSubArraysWithinBounds()
    print(s.countSubarrays([1, 1, 1, 1], 1, 1))
    print(s.countSubarrays([1, 3, 5, 2, 7, 5], 1, 5))
