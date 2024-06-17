# Problem 257

from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTreePaths:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        running = []
        result = []
        self.recurse(root, running, result)
        return result

    def recurse(self, node: TreeNode, running: List[str], result: List[str]):
        running.append(str(node.val))
        if node.left is None and node.right is None:
            result.append('->'.join(running))
            return

        if node.left is not None:
            running_copy = list(running)
            self.recurse(node.left, running_copy, result)
        if node.right is not None:
            running_copy2 = list(running)
            self.recurse(node.right, running_copy2, result)
