# Problem 606
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right 

class ConstructStringFromBinaryTree:
    
        def tree2str(self, root: Optional[TreeNode]) -> str:
            return self.preorder(root)
            
        def preorder(self, present: TreeNode) -> str:
            presentstring = ""
            if present.val is not None:
                presentstring = presentstring + str(present.val)
            if present.left is not None or present.right is not None:
                
                presentstring = presentstring + "("
                if present.left is not None:
                    presentstring = presentstring + self.preorder(present.left)
                presentstring = presentstring + ")"

                
                if present.right is not None:
                    presentstring = presentstring + "("
                    presentstring = presentstring + self.preorder(present.right)
                    presentstring = presentstring + ")"
            return presentstring
    
if __name__ == '__main__':
    c = ConstructStringFromBinaryTree()
