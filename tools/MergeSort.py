# Check Problem 912
from typing import List


class MergeSort:

    def sortArray(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        self.split_merge(nums, 0, len(nums) - 1, res)
        return nums

    def split_merge(self, arr: List[int], s: int, e: int, res: List[int]):
        if s == e:
            return
        elif s == e - 1:
            if arr[s] > arr[e]:
                temp = arr[s]
                arr[s] = arr[e]
                arr[e] = temp
            return

        m = (s + e) // 2
        self.split_merge(arr, s, m, res)
        self.split_merge(arr, m + 1, e, res)
        self.merge(arr, s, m, e, res)

    def merge(self, arr: List[int], s: int, m: int, e: int, res: List[int]):
        l, r = s, m + 1

        for i in range(s, e + 1):
            if l == m + 1:  # end of left reached
                res[i] = arr[r]
                r += 1
            elif r == e + 1:  # end of right reached
                res[i] = arr[l]
                l += 1
            else:
                if arr[l] > arr[r]:
                    res[i] = arr[r]
                    r += 1
                else:
                    res[i] = arr[l]
                    l += 1

        for i in range(s, e + 1):
            arr[i] = res[i]


m = MergeSort()
print(m.sortArray([5, 1, 1, 2, 0, 0]))
