# Problem 2331

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class EvaluateBooleanBinaryTree:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        return self.recurse(root)

    def recurse(self, node: TreeNode) -> bool:
        if not node.left:
            return node.val == 1
        lhs, rhs = self.recurse(node.left), self.recurse(node.right)
        return lhs | rhs if node.val == 2 else lhs & rhs
