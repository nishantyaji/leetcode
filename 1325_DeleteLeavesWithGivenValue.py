# Problem 1325

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class DeleteLeavesWithGivenValue:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if not root:
            return root
        return self.recurse(root, target)

    def recurse(self, node: TreeNode, target: int) -> Optional[TreeNode]:
        if node.left is not None:
            node.left = self.recurse(node.left, target)
        if node.right is not None:
            node.right = self.recurse(node.right, target)

        if node.left is None and node.right is None and target == node.val:
            return None
        else:
            return node
