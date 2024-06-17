# Problem 113

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class PathSumII:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return []

        result = []
        running_list = []
        running = 0
        self.recurse(root, targetSum, running, running_list, result)
        return result

    def recurse(self, node: TreeNode, desired: int, running: int, running_list: List[int], result: List[List[int]]):
        running += node.val
        running_list.append(node.val)
        if node.left is None and node.right is None:
            if running == desired:
                result.append(running_list)

        if node.left is not None:
            self.recurse(node.left, desired, running, list(running_list), result)
        if node.right is not None:
            self.recurse(node.right, desired, running, list(running_list), result)
