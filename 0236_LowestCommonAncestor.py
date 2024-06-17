# Problem 236
# This is a very complicated solution. Forgive me. I know there is a more elegant solution.
# This script is ripe for revising
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class LowestCommonAncestor:

    def form_tree(self, input_ints: List[int]) -> TreeNode:
        input_list = []
        for i in input_ints:
            if i is None:
                input_list.append(None)
            else:
                elem = TreeNode(i)
                input_list.append(elem)

        parent_size_limit = int(len(input_ints) / 2)
        for i in range(0, parent_size_limit):
            if input_list[i] is not None:
                input_list[i].left = input_list[2 * i + 1]
                if 2 * i + 2 < len(input_ints):
                    input_list[i].right = input_list[2 * i + 2]

        return input_list[0]

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val == q.val:
            return p

        startValue, destValue = p.val, q.val

        left_start_str = right_start_str = left_dest_str = right_dest_str = ""
        if root.left is not None:
            left_start_str = self.recurse(root.left, startValue, True)
            left_dest_str = self.recurse(root.left, destValue, True)

        if root.right is not None:
            right_start_str = self.recurse(root.right, startValue, False)
            right_dest_str = self.recurse(root.right, destValue, False)

        start_path = left_start_str if len(left_start_str) else right_start_str
        dest_path = left_dest_str if len(left_dest_str) else right_dest_str

        if start_path.find(dest_path) == 0:
            return q

        if dest_path.find(start_path) == 0:
            return p

        node = root
        for i in range(0, min(len(start_path), len(dest_path))):
            if start_path[i] == dest_path[i]:
                node = node.left if start_path[i] == "L" else node.right
            else:
                break

        return node

    def recurse(self, node: TreeNode, req: int, is_left: bool) -> str:
        present_val = "L" if is_left else "R"
        if node.val == req:
            return present_val
        if node.left is None and node.right is None:
            return ""
        left_str = right_str = ""
        if node.left is not None:
            left_str = self.recurse(node.left, req, True)
        if node.right is not None:
            right_str = self.recurse(node.right, req, False)

        if len(left_str) > 0:
            return present_val + left_str
        if len(right_str) > 0:
            return present_val + right_str
        return ""


if __name__ == '__main__':
    l = LowestCommonAncestor()
    # print(l.lowestCommonAncestor(l.form_tree(), ,))
    print(l.lowestCommonAncestor(l.form_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]), TreeNode(6), TreeNode(0)).val)
    print(l.lowestCommonAncestor(l.form_tree([-1, 0, 3, -2, 4, None, None, 8]), TreeNode(8), TreeNode(4)).val)
    print(l.lowestCommonAncestor(l.form_tree([1, 2, 3, None, 4]), TreeNode(4), TreeNode(3)).val)
