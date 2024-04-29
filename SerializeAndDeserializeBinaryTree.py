# Problem 297

import math
from typing import List


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class SerializeAndDeserializeBinaryTree:

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

    def dfs(self, root):
        if root is None:
            return 0
        left_depth = self.dfs(root.left)
        right_depth = self.dfs(root.right)
        return 1 + max(left_depth, right_depth)

    def serialize(self, root):
        if root is None:
            return ""
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        q = [[0, root]]

        depth = self.dfs(root)
        capacity = (int(math.pow(2, depth)) - 1)
        res = [[0, root.val]]
        while q and capacity > 1:
            [i, node] = q.pop(0)
            if node is not None:
                if node.left is not None:
                    q.append([2 * i + 1, node.left])
                    res.append([2 * i + 1, node.left.val])
                if node.right is not None:
                    q.append([2 * i + 2, node.right])
                    res.append([2 * i + 2, node.right.val])

        res_copy = []
        for x in res:
            res_copy.append(str(x[0]) + ":" + str(x[1]))
        return "|".join(res_copy)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data is None or data == "":
            return None
        input_ints = data.split("|")
        my_dict = {}
        for i in input_ints:
            tokens = i.split(":")
            my_dict[int(tokens[0])] = int(tokens[1])

        q = [0]
        root = TreeNode(my_dict[0])
        copy_dict = {0: root}
        while q:
            index = q.pop(0)
            node = copy_dict[index]
            copy_dict[index] = node
            if (2 * index + 1) in my_dict:
                left_node = TreeNode(my_dict[2 * index + 1])
                node.left = left_node
                copy_dict[2 * index + 1] = left_node
                q.append(2 * index + 1)
            if (2 * index + 2) in my_dict:
                right_node = TreeNode(my_dict[2 * index + 2])
                node.right = right_node
                copy_dict[2 * index + 2] = right_node
                q.append(2 * index + 2)
            del copy_dict[index]

        return root


if __name__ == '__main__':
    s = SerializeAndDeserializeBinaryTree()
    print(s.serialize(s.form_tree([1])))
    print(s.serialize(s.form_tree([1, 2, 3, None, None, 4, 5])))

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
