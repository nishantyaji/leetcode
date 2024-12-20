# Problem 2415
import collections
from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class ReverseOddLevelsOfBinTree:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            mp = collections.defaultdict(deque)
            self.recurse(root, mp, 0)
            self.assign(root, mp, 0)
        return root

    def recurse(self, node: TreeNode, mp, depth):
        mp[depth].append(node.val)
        if node.left:
            self.recurse(node.left, mp, depth + 1)
        if node.right:
            self.recurse(node.right, mp, depth + 1)

    def assign(self, node: TreeNode, mp, depth):
        node.val = mp[depth].pop() if depth % 2 == 1 else mp[depth].popleft()
        if node.left:
            self.assign(node.left, mp, depth + 1)
        if node.right:
            self.assign(node.right, mp, depth + 1)
