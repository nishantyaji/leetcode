# Problem 129

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class SumRootToLeafNumbers:  
    sumAll = 0
    def __init__(self):
        sumAll = 0

    def sumNumbers(self, root: Optional[TreeNode]) -> int: 
        if root is None:
            return 0
        self.recurse(root, 0)
        return self.sumAll
        
    def recurse(self, present: Optional[TreeNode], val: int):
        
        newval = 10 * val + present.val 
        if present.left is None and present.right is None:
            temp = self.sumAll + newval
            self.sumAll = temp
        else:
            if present.left is not None:
                self.recurse(present.left, newval)
            if present.right is not None:
                self.recurse(present.right, newval)

if __name__ == '__main__':
    s = SumRootToLeafNumbers()  
