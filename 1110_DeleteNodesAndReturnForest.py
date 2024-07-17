# Problem 1110
import collections
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        if not root or (not root.left and not root.right):
            return []
        par_dict, child_dict = {root.val: (None, None)}, collections.defaultdict(list)
        self.recurse(root, par_dict, child_dict)
        forests = [root] if root.val not in to_delete else []
        for node in to_delete:
            parent, is_left = par_dict[node]
            if parent:
                if is_left:
                    parent.left = None
                else:
                    parent.right = None
            forests = forests + list(filter(lambda x: x.val not in to_delete, child_dict[node]))
        return forests

    def recurse(self, node: TreeNode, par_dict: dict, child_dict: dict):
        if node.left:
            child_dict[node.val].append(node.left)
            par_dict[node.left.val] = (node, True)
            self.recurse(node.left, par_dict, child_dict)
        if node.right:
            child_dict[node.val].append(node.right)
            par_dict[node.right.val] = (node, False)
            self.recurse(node.right, par_dict, child_dict)
