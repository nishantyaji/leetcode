# Problem 110

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BalancedBinaryTree:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self.depth(root)[0]

    def depth(self, root):
        if root is None:
            return [True, 0]

        left_depth, right_depth = 0, 0
        l_status, r_status = True, True
        if root.left is not None:
            [l_status, left_depth] = self.depth(root.left)
        if root.right is not None:
            [r_status, right_depth] = self.depth(root.right)
        return [(l_status and r_status) and abs(left_depth - right_depth) <= 1, max(left_depth, right_depth) + 1]
