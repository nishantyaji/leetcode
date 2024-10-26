# Problem 2458
import copy
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class HeightBinTreeAfterSubtreeRemovalQueries:

    def __init__(self):
        self.node_level = {}
        self.level_heights = {}
        self.max_height = {}

    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        self.iterate(root, 0)

        def find_val(numm: int):
            this_dict = copy.deepcopy(self.level_heights[self.node_level[numm]])
            this_dict[self.max_height[numm]] -= 1
            others = [k for k, v in this_dict.items() if v > 0]
            if not others:
                return self.node_level[numm] - 1
            return max(others)

        return [find_val(q) for q in queries]

    def iterate(self, node: TreeNode, depth):
        if not node:
            return depth - 1
        self.node_level[node.val] = depth

        lhs = self.iterate(node.left, depth + 1)
        rhs = self.iterate(node.right, depth + 1)
        height = max(lhs, rhs)
        self.max_height[node.val] = height
        if depth not in self.level_heights:
            self.level_heights[depth] = {}
        if height not in self.level_heights[depth]:
            self.level_heights[depth][height] = 0
        self.level_heights[depth][height] += 1
        return height
