# Problem 1123
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class LowestCommonAncestorOfDeepestLeaves:

    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        mp = {}
        self.calc_depth(root, 0, mp)
        max_depth = max(mp.keys())
        temp = self.find_lca(root, 0, max_depth, mp[max_depth])
        return temp[0]

    def calc_depth(self, node: TreeNode, depth: int, mp: dict):
        if node.left is None and node.right is None:
            if depth not in mp:
                mp[depth] = 0
            mp[depth] += 1
            return

        if node.left:
            self.calc_depth(node.left, depth + 1, mp)
        if node.right:
            self.calc_depth(node.right, depth + 1, mp)

    def find_lca(self, node: TreeNode, depth: int, max_depth: int, target: int):
        if node.left is None and node.right is None:
            if depth == max_depth:
                if target == 1:
                    return [node, 1]
                else:
                    return [None, 1]

        this_val = 0
        if node.left:
            temp = self.find_lca(node.left, depth + 1, max_depth, target)
            if temp[0] is not None:
                return temp
            else:
                this_val += temp[1]
        if node.right:
            temp = self.find_lca(node.right, depth + 1, max_depth, target)
            if temp[0] is not None:
                return temp
            else:
                this_val += temp[1]

        if target == this_val:
            return [node, this_val]
        else:
            return [None, this_val]
