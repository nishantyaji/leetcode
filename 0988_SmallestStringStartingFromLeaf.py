# Problem 988

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SmallestStringStartingFromLeaf:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return ""
        mylist = list()
        self.recurse(root, "", mylist)
        mylist.sort()
        return mylist[0]

    def recurse(self, node: TreeNode, running: str, mylist: list):
        running_copy = str(running)
        running_copy = running_copy + chr(ord('a') + node.val)
        if node.left is None and node.right is None:
            mylist.append(running_copy[::-1])
            return

        if node.left is not None:
            self.recurse(node.left, running_copy, mylist)
        if node.right is not None:
            self.recurse(node.right, running_copy, mylist)
