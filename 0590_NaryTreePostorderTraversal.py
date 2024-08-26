# Problem 590
from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class NaryTreePostorderTraversal:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        if root:
            self.recurse(root, res)
        return res

    def recurse(self, node: 'Node', res: List[int]):
        if node.children:
            for c in node.children:
                if c:
                    self.recurse(c, res)

        res.append(node.val)
        return res
