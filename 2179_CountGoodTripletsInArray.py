# Problem 2179
from typing import List


class BinaryIndexedTree:
    def __init__(self, size):
        self.n = size
        self.tree = [0] * (self.n + 1)  # Note: 1-indexed

    def update(self, index, delta):
        index += 1
        while index <= self.n:
            self.tree[index] += delta
            index += index & -index

    def query(self, index):
        index += 1
        result = 0
        while index > 0:
            result += self.tree[index]
            index -= index & -index
        return result


class CountGoodTripletsInArray:

    def get_vals(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mp = {x: i for i, x in enumerate(nums1)}

        bit1 = BinaryIndexedTree(len(nums1))
        vals = [0] * len(nums1)
        for i, n in enumerate(nums2):
            temp = bit1.query(mp[n] - 1)
            vals[i] = temp
            bit1.update(mp[n], 1)
        return vals

    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        left_vals = self.get_vals(nums1, nums2)
        right_vals = self.get_vals(nums1[::-1], nums2[::-1])[::-1]
        return sum([left_vals[i] * right_vals[i] for i in range(len(nums1))])
