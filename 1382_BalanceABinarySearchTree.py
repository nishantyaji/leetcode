# Problem 1382


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BalanceABinarySearchTree:

    def __init__(self):
        self.lst = []

    def balanceBST(self, root: TreeNode) -> TreeNode:
        self.recurse(root)
        return self.build(0, len(self.lst) - 1)

    def build(self, i: int, j: int) -> TreeNode:
        if i == j:
            return TreeNode(self.lst[i], None, None)
        elif i == j - 1:
            return TreeNode(self.lst[i], None, TreeNode(self.lst[j]))

        # i and j are inclusive
        mid = (i + j) // 2
        return TreeNode(self.lst[mid], self.build(i, mid - 1), self.build(mid + 1, j))

    def recurse(self, node: TreeNode):
        if not node.left and not node.right:
            self.lst.append(node.val)
            return
        if node.left:
            self.recurse(node.left)
        self.lst.append(node.val)
        if node.right:
            self.recurse(node.right)


if __name__ == '__main__':
    b = BalanceABinarySearchTree()
