# Problem 2641
import collections
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class CousinsInBinTreeII:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            mp = collections.defaultdict(int)
            self.recur(root, 2, mp)
            root.val = 0
            self.realloc(root, 2, mp)
        return root

    def recur(self, node: TreeNode, depth: int, mp: dict):
        if node.left:
            mp[depth] += node.left.val
            self.recur(node.left, depth + 1, mp)
        if node.right:
            mp[depth] += node.right.val
            self.recur(node.right, depth + 1, mp)

    def realloc(self, node: TreeNode, depth: int, mp: dict):
        lhs = 0 if not node.left else node.left.val
        rhs = 0 if not node.right else node.right.val
        for new_node in [node.left, node.right]:
            if new_node:
                new_node.val = mp[depth] - (lhs + rhs)
                self.realloc(new_node, depth + 1, mp)
