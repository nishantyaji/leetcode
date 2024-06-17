#Problem 404
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SumOfLeftLeaves:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        mylist = []
        self.recurse(root, False, mylist)
        return sum(mylist)

    def recurse(self, node: Optional[TreeNode], is_left: bool, mylist: list) -> int:
        is_leaf = node.left is None and node.right is None
        if is_leaf and is_left:
            mylist.append(node.val)

        if node.left:
            self.recurse(node.left, True, mylist)
        if node.right:
            self.recurse(node.right, False, mylist)
