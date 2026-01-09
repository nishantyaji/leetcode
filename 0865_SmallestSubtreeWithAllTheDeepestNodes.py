# Problem 865
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SmallestSubtreeWithAllTheDeepestNodes:

    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        d = self.recurse(root)
        s = set()
        self.find(root, 1, d, s)
        res, l = self.sweep(root, s)
        return res

    def recurse(self, node: TreeNode):
        l, r = 0, 0
        if node.left:
            l = self.recurse(node.left)
        if node.right:
            r = self.recurse(node.right)
        return 1 + max(l, r)

    def find(self, node: TreeNode, depth: int, d: int, s: set):
        if d == depth:
            s.add(node.val)
        if node.left:
            self.find(node.left, depth + 1, d, s)
        if node.right:
            self.find(node.right, depth + 1, d, s)

    def sweep(self, node: TreeNode, s: set):
        if node.val in s:
            if len(s) == 1:
                return node, 1
            return None, 1
        l, r, nl, nr = 0, 0, None, None
        if node.left:
            nl, l = self.sweep(node.left, s)
        if node.right:
            nr, r = self.sweep(node.right, s)

        if nl:
            return nl, len(s)
        if nr:
            return nr, len(s)

        if l + r == len(s):
            return node, l + r

        return None, l + r
