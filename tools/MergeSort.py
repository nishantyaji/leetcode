# Check Problem 912
from typing import List


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


def max_(self, arr: List[int]) -> int:
    if len(arr) == 1:
        return arr[0]
    return arr[0] if arr[0] > arr[1] else arr[1]


def merge(self, arr: List[int], s: int, m: int, e: int, res: List[int]):
    l, r = s, m + 1

    for i in range(s, e + 1):
        if l == m + 1: # end of left reached
            res[i] = arr[r]
            r += 1
        elif r == e + 1: # end of right reached
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


# print(sortArray([5, 2, 3, 1]))
# print(sortArray([5, 1, 1, 2, 0, 0]))
