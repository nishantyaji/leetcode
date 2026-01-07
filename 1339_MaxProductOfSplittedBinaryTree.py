# Problem 1339
import functools
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class MaxProductOfSplittedBinaryTree:

    def maxProduct(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        all_total = self.summation(root)
        print("total: ", all_total)
        res = [-1]
        self.recurse(root, all_total, res)
        return res[0] % 1000000007

    @functools.cache
    def summation(self, node: TreeNode):
        res = node.val
        if node.left:
            res += self.summation(node.left)
        if node.right:
            res += self.summation(node.right)
        return res

    def recurse(self, node: TreeNode, all_total: int, max_val: list[int]):
        if node.left:
            left = self.summation(node.left)
            temp = ((all_total - left) * left)
            if max_val[0] < temp:
                max_val[0] = temp
            self.recurse(node.left, all_total, max_val)
        if node.right:
            right = self.summation(node.right)
            temp = ((all_total - right) * right)
            if max_val[0] < temp:
                max_val[0] = temp
            self.recurse(node.right, all_total, max_val)
