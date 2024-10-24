# Problem 951
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class FlipEquivalentBinTrees:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True
        if (not root1 and root2) or (not root2 and root1) or root1.val != root2.val:
            return False
        root1_ch = [] if not root1 else [x for x in [root1.left, root1.right] if x]
        root2_ch = [] if not root2 else [x for x in [root2.left, root2.right] if x]
        if len(root1_ch) != len(root2_ch):
            return False

        root1_ch.sort(key=lambda x: x.val)
        root2_ch.sort(key=lambda x: x.val)
        res = True
        for i in range(len(root1_ch)):
            res = res and self.flipEquiv(root1_ch[i], root2_ch[i])
        return res
