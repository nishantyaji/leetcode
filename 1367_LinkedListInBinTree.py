# Problem 1367
import copy
from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class LinkedListInBinTree:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if head is None or root is None:
            return False

        req = ""
        while head is not None:
            req += str(head.val)
            head = head.next

        run, result = "", []
        self.recurse(root, run, result)
        for r in result:
            if req in r:
                return True
        return False

    def recurse(self, node: TreeNode, run: str, result: List[str]):
        run = run + str(node.val)
        if node.left is None and node.right is None:
            result.append(run)
            return

        if node.left:
            self.recurse(node.left, copy.deepcopy(run), result)
        if node.right:
            self.recurse(node.right, copy.deepcopy(run), result)
