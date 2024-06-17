# Problem 129

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        leaf_list = []
        self.recurse(root, 0, leaf_list)
        return sum(leaf_list)

    def recurse(self, node: TreeNode, running: int, leaf_list: list):
        if node.left is None and node.right is None:
            leaf_list.append(10 * running + node.val)
            return

        if node.left is not None:
            self.recurse(node.left, 10 * running + node.val, leaf_list)
        if node.right is not None:
            self.recurse(node.right, 10 * running + node.val, leaf_list)
