# Problem 1038
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinarySearchTreeToGreaterSumTree:

    def __init__(self):
        # this is critical
        # otherwise things get messy while dealing with return values
        self.run_sum = 0

    def bstToGst(self, root: TreeNode) -> TreeNode:
        if not root.left and not root.right:
            return root
        self.recurse(root)

    def recurse(self, node: TreeNode):
        if node.right is not None:
            self.recurse(node.right)
        self.run_sum += node.val
        node.val = self.run_sum
        if node.left is not None:
            self.recurse(node.left)


if __name__ == '__main__':
    b = BinarySearchTreeToGreaterSumTree()
