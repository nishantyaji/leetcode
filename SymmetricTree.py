# Problem 101
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class SymmetricTree:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        if (root.left is None and root.right is not None) or (root.left is not None and root.right is None):
            return False
        elif root.left is None and root.right is None:
            return True
        else:
            return self.areEqual(root.left, root.right)
        
    def areEqual(self, leftside: TreeNode, rightside: TreeNode) -> bool:
        if leftside.val != rightside.val:
            return False
        
        if leftside.left is None and rightside.right is None:
            #do nothing
            pass 
        elif leftside.left is not None and rightside.right is not None:
            if self.areEqual(leftside.left, rightside.right) == False:
                return False
        else:
            return False
        
        if leftside.right is None and rightside.left is None:
            #do nothing
            pass
        elif leftside.right is not None and rightside.left is not None:
            if self.areEqual(leftside.right, rightside.left) == False:
                return False
        else:
            return False
        
        return True
    
if __name__ == '__main__':
    s = SymmetricTree()