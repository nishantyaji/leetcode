# Problem 1261
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.st = set()
        self.root = root
        self.recurse(self.root, self.st)

    def recurse(self, node: TreeNode, st: set):
        if node.val == -1:
            node.val = 0
            st.add(0)
        if node.left and node.left.val == -1:
            node.left.val = 2 * node.val + 1
            st.add(node.left.val)
            self.recurse(node.left, st)
        if node.right and node.right.val == -1:
            node.right.val = 2 * node.val + 2
            st.add(node.right.val)
            self.recurse(node.right, st)

    def find(self, target: int) -> bool:
        return target in self.st

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
