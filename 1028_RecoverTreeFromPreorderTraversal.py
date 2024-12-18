# Problem 1028
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class RecoverTreeFromPreorderTraversal:

    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        if not traversal:
            return None
        my_dict = {}
        head, prev = None, None
        d_count = 0
        depth = 0
        run_str = ""
        for x in traversal:
            if x == "-":
                if d_count == 0:
                    temp_node = TreeNode(int(run_str))
                    if not head:
                        head = temp_node
                        my_dict[0] = temp_node
                    else:
                        par = my_dict[depth - 1]
                        if not par.left:
                            par.left = temp_node
                        else:
                            par.right = temp_node
                        my_dict[depth] = temp_node
                run_str = ""
                d_count += 1
            else:
                if d_count:
                    depth = d_count
                d_count = 0
                run_str += x

        temp_node = TreeNode(int(run_str))
        if not head:
            head = temp_node
            my_dict[0] = temp_node
        else:
            par = my_dict[depth - 1]
            if not par.left:
                par.left = temp_node
            else:
                par.right = temp_node
            my_dict[depth] = temp_node
        return head


if __name__ == '__main__':
    r = RecoverTreeFromPreorderTraversal()
    print(r.recoverFromPreorder("3"))
    print(r.recoverFromPreorder("1-2--3--4-5--6--7"))
    print(r.recoverFromPreorder("1-2--3---4-5--6---7"))
    print(r.recoverFromPreorder("1-401--349---90--88"))
