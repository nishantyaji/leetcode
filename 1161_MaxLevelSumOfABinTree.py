# Problem 1161
import collections
import sys
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class MaxLevelSumOfABinTree:
    class Solution:
        def maxLevelSum(self, root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            mp = collections.defaultdict(int)
            self.recurse(root, 1, mp)
            mx, idx = -sys.maxsize, -1
            for i, m in mp.items():
                if m > mx:
                    idx = i
                    mx = m
            return idx

        def recurse(self, node: TreeNode, depth: int, mp: dict):
            mp[depth] += node.val
            if node.left:
                self.recurse(node.left, depth + 1, mp)
            if node.right:
                self.recurse(node.right, depth + 1, mp)
