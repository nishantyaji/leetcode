# Problem 814

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTreePruning:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
        return self.recurse(root)

    def recurse(self, node: TreeNode) -> Optional[TreeNode]:
        if node.left is not None:
            node.left = self.recurse(node.left)
        if node.right is not None:
            node.right = self.recurse(node.right)

        if node.left is None and node.right is None:
            return node if node.val == 1 else None

        return node
