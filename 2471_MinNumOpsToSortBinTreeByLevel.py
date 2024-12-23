# Problem 2471
import collections
import copy
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class MinNumOpsToSortBinTreeByLevel:

    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        mp = collections.defaultdict(list)
        self.recurse(root, mp, 0)
        res = 0
        for k, v in mp.items():
            res += self.count_inversions(v)
            print(k, ";", res)
        return res

    def recurse(self, node, mp, depth):
        mp[depth].append(node.val)
        if node.left:
            self.recurse(node.left, mp, depth + 1)
        if node.right:
            self.recurse(node.right, mp, depth + 1)

    def count_inversions(self, nums):
        # note to self : formulate a better algo
        nums_copy = copy.deepcopy(nums)
        nums_copy.sort()
        res = 0
        my_dict = {x: i for i, x in enumerate(nums)}
        for i in range(len(nums)):
            if nums_copy[i] != nums[i]:
                temp = nums[i]
                temp_pos = my_dict[nums_copy[i]]
                nums[temp_pos] = temp
                nums[i] = nums_copy[i]
                my_dict[nums[i]] = i
                my_dict[temp] = temp_pos
                res += 1

        return res
