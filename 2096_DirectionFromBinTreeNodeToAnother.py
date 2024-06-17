# Problem 2096

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class DirectionFromBinTreeNodeToAnother:

    def form_tree(self, input_ints: List[int]) -> TreeNode:
        input_list = []
        for i in input_ints:
            if i is None:
                input_list.append(None)
            else:
                elem = TreeNode(i, None, None)
                input_list.append(elem)

        parent_size_limit = int(len(input_ints) / 2)
        for i in range(0, parent_size_limit):
            if input_list[i] is not None:
                input_list[i].left = input_list[2 * i + 1]
                if 2 * i + 2 < len(input_ints):
                    input_list[i].right = input_list[2 * i + 2]

        return input_list[0]

    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        if startValue == destValue or root is None:
            return ""
        left_start_str = right_start_str = left_dest_str = right_dest_str = ""
        if root.left is not None:
            left_start_str = self.recurse(root.left, startValue, True)
            left_dest_str = self.recurse(root.left, destValue, True)

        if root.right is not None:
            right_start_str = self.recurse(root.right, startValue, False)
            right_dest_str = self.recurse(root.right, destValue, False)

        start_path = left_start_str if len(left_start_str) else right_start_str
        dest_path = left_dest_str if len(left_dest_str) else right_dest_str
        count = 0
        for i in range(0, min(len(start_path), len(dest_path))):
            if len(start_path) == 0 or len(dest_path) == 0 or start_path[i] != dest_path[i]:
                break
            count += 1

        start_path = start_path[count:]
        dest_path = dest_path[count:]

        return "U" * len(start_path) + dest_path

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
    d = DirectionFromBinTreeNodeToAnother()

    # U
    print(d.getDirections(d.form_tree([5, 8, 3, 1, None, 4, 7, 6, None, None, None, None, None, None, 2]), 4, 3))

    # UURL
    print((d.getDirections(d.form_tree([5, 1, 2, 3, None, 6, 4]), 3, 6)))
