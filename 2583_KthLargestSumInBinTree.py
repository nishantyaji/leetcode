# Problem 2583
import collections
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class KthLargestSumInBinTree:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1
        mp = collections.defaultdict(int)
        mp[1] += root.val
        self.recur(root, 2, mp)
        if len(mp) < k:
            return -1
        vals = sorted(mp.values(), reverse=True)
        return vals[k - 1]

    def recur(self, node: TreeNode, depth: int, mp: dict):
        if node.left:
            mp[depth] += node.left.val
            self.recur(node.left, depth + 1, mp)
        if node.right:
            mp[depth] += node.right.val
            self.recur(node.right, depth + 1, mp)
