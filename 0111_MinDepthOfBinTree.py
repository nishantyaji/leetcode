# Problem 111

from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class MinDepthPfBinTree:

    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1

        min_depth = 1000001
        if root.left is not None:
            min_depth = min(min_depth, self.minDepth(root.left))
        if root.right is not None:
            min_depth = min(min_depth, self.minDepth(root.right))

        return min_depth + 1
