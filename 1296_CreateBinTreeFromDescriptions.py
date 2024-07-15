# Problem 2196
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class CreateBinTreeFromDescriptions:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        mp, parent_set, children_set = dict(), set(), set()
        for d in descriptions:
            [parent, child, is_left] = d
            parent_set.add(parent)
            children_set.add(child)
            if parent not in mp:
                mp[parent] = TreeNode(parent)
            if child not in mp:
                mp[child] = TreeNode(child)

            if is_left == 1:
                mp[parent].left = mp[child]
            else:
                mp[parent].right = mp[child]
        return mp[list(parent_set - children_set)[0]]


if __name__ == '__main__':
    c = CreateBinTreeFromDescriptions()
    print(c.createBinaryTree([[20, 15, 1], [20, 17, 0], [50, 20, 1], [50, 80, 0], [80, 19, 1]]))
    print(c.createBinaryTree([[1, 2, 1], [2, 3, 0], [3, 4, 1]]))
