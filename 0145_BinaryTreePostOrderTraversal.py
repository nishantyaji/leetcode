# Problem 145
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTreePostOrderTraversal:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if root:
            self.recurse(root, res)
        return res

    def recurse(self, node: TreeNode, res: List[int]):
        if node.left:
            self.recurse(node.left, res)
        if node.right:
            self.recurse(node.right, res)
        res.append(node.val)
