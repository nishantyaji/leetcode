# Problem 515
import sys
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = [-sys.maxsize] * 1000
        d = [-sys.maxsize]
        self.recurse(root, res, 0, d)
        return res[:d[0] + 1]

    def recurse(self, node: TreeNode, res: list[int], depth: int, d: list[int]):
        res[depth] = max(node.val, res[depth])
        d[0] = max(depth, d[0])
        if node.left:
            self.recurse(node.left, res, depth + 1, d)
        if node.right:
            self.recurse(node.right, res, depth + 1, d)
