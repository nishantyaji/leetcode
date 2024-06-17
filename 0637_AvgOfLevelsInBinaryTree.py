# Problem 637
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class AvgOfLevelsInBinaryTree:
    
    def __init__(self):
        self.vals_per_level = {}
        self.rootobjects = []

    def formTree(self, root: Optional[TreeNode]):
        for i in range(0, len(root)):
            temp = TreeNode(root[i]) if root[i] is not None else None
            self.rootobjects.append(temp)
            if i != 0:
                parent = (int) ((i-1)/2)
                if i % 2 == 1:
                    self.rootobjects[parent].left = temp
                else:
                    self.rootobjects[parent].right = temp

        return self.rootobjects[0]


    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root is None:
            return []
        # self.traverse(root, 0)
        self.traverse(self.formTree(root), 0)
        ans = [self.vals_per_level[x][0] for x in range(0, len(self.vals_per_level)) ]
        self.vals_per_level = {}
        self.rootobjects = []
        return ans


    def traverse(self, node: TreeNode, depth: int) :
        if node is not None:
            if len(self.vals_per_level) < depth + 1 or len(self.vals_per_level[depth]) == 0:
                self.vals_per_level[depth] = [node.val, 1]
            else:
                new_avg = (self.vals_per_level[depth][0] * self.vals_per_level[depth][1] + node.val ) / (self.vals_per_level[depth][1] + 1)
                new_count = self.vals_per_level[depth][1] + 1
                self.vals_per_level[depth] = [new_avg, new_count]

            if node.left is not None:
                self.traverse(node.left, depth + 1)
            if node.right is not None:
                self.traverse(node.right, depth + 1)

if __name__ == '__main__':
    a = AvgOfLevelsInBinaryTree()
    print(a.averageOfLevels([5,2,-3]))
    a = AvgOfLevelsInBinaryTree()
    print(a.averageOfLevels([3,9,20,15,7]))
    a = AvgOfLevelsInBinaryTree()
    print(a.averageOfLevels([3,9,20,None,None,15,7]))
    