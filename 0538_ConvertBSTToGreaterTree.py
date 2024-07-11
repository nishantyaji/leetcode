# Problem 538
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.run_sum = 0

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
        if not root.left and not root.right:
            return root
        self.recurse(root)
        return root

    def recurse(self, node: TreeNode):
        if node.right is not None:
            self.recurse(node.right)
        self.run_sum += node.val
        node.val = self.run_sum
        if node.left is not None:
            self.recurse(node.left)
