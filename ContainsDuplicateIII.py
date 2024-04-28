# Problem 220

from typing import List


class ContainsDuplicateIII:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:

        window = []
        for i in range(0, min(indexDiff + 1, len(nums))):
            window.append(nums[i])
        window.sort()
        for i in range(0, len(window)-1):
            if abs(window[i] - window[i + 1]) <= valueDiff:
                return True

        for i in range(indexDiff + 1, len(nums)):
            window = self.delete(window, nums[i - indexDiff - 1])
            [ins_idx, window] = self.insert(window, nums[i])
            if self.checkCondition(window, valueDiff, ins_idx):
                return True
        return False

    def checkCondition(self, window: List[int], diff: int, ins_idx: int) -> bool:
        for i in range(max(0, ins_idx - 1), max(ins_idx+1, len(window) - 1)):
            if abs(window[i] - window[i + 1]) <= diff:
                return True
        return False

    def delete(self, window: List[int], num: int):
        #Can be optimized, especially the if conditions
        [low, high] = [0, len(window) - 1]
        req_idx = -1
        while low + 1 < high:
            mid = int((low + high) / 2)
            if window[mid] == num:
                req_idx = mid
                break
            if window[mid] > num:
                [low, high] = [low, mid]
            else:
                [low, high] = [mid, high]

        idx = None
        if req_idx != -1:
            idx = req_idx
        if window[low] == num:
            idx = low
        if window[high] == num:
            idx = high

        if idx is not None:
            return window[:idx] + window[idx + 1:]

        return  window

    def insert(self, window: List[int], num: int):
        #Can be optimized, especially the if conditions
        [low, high] = [0, len(window) - 1]
        req_idx = -1

        while low + 1 < high:
            mid = int((low + high) / 2)
            if window[mid] == num:
                req_idx = mid
                break
            if window[mid] > num:
                [low, high] = [low, mid]
            else:
                [low, high] = [mid, high]

        if req_idx == -1:
            req_idx = low

        return [req_idx, window[:req_idx + 1] + [num] + window[req_idx + 1:]]


if __name__ == '__main__':
    c = ContainsDuplicateIII()
    # print(c.delete([1, 2, 3, 3, 4, 5, 6], 6))
    # print(c.delete([1, 2, 3, 3, 4, 5, 6], 1))
    # print(c.delete([1, 2, 3, 3, 4, 5, 6], 3))
    # print(c.delete([1, 2, 3, 3, 4, 5, 6], 4))
    # print(c.insert([1, 2, 3, 3, 4, 5, 6], 4))
    # print(c.insert([1, 2, 30, 31, 42, 50, 61], 41))
    print(c.containsNearbyAlmostDuplicate([-3, 3], 2, 4))
    print(c.containsNearbyAlmostDuplicate([1, 2, 3, 1], 3, 0))
    print(c.containsNearbyAlmostDuplicate([1, 5, 9, 1, 5, 9], 2, 3))
