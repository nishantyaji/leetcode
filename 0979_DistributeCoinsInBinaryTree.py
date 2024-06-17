# Problem 979

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class DistributeCoinsInBinaryTree:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return self.recurse(root)[1]

    def recurse(self, node: TreeNode):
        if node.left is None and node.right is None:
            return [node.val - 1, abs(node.val - 1)]

        lhs, rhs = [0, 0], [0, 0]
        if node.left is not None:
            lhs = self.recurse(node.left)
        if node.right is not None:
            rhs = self.recurse(node.right)

        coins = lhs[0] + rhs[0] + node.val - 1
        moves = abs(coins) + lhs[1] + rhs[1]
        return [coins, moves]
