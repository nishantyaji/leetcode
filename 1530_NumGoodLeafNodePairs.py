# Problem 1530
import collections
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class NumGoodLeafNodePairs:

    def form_tree(self, input_ints: List[int]) -> TreeNode:
        input_list = [None if i is None else TreeNode(i, None, None) for i in input_ints]

        parent_size_limit = len(input_ints) // 2
        for i in range(0, parent_size_limit):
            if input_list[i] is not None:
                input_list[i].left = input_list[2 * i + 1]
                if 2 * i + 2 < len(input_ints):
                    input_list[i].right = input_list[2 * i + 2]

        return input_list[0]

    def countPairs(self, root: TreeNode, distance: int) -> int:
        result = [0]
        self.recurse(root, distance, result)
        return result[0]

    def recurse(self, node: TreeNode, distance: int, result: List[int]):
        if not node:
            return dict()
        if not node.left and not node.right:
            return {0: 1}

        l_dict = self.incr(self.recurse(node.left, distance, result))
        r_dict = self.incr(self.recurse(node.right, distance, result))

        for kl, vl in l_dict.items():
            for kr, vr in r_dict.items():
                if 0 < kl < distance and 0 < kr < distance and (kl + kr) <= distance:
                    result[0] += vl * vr
        return self.merge(l_dict, r_dict)

    def merge(self, d1: dict, d2: dict):
        d = collections.defaultdict(int)
        for temp in [d1, d2]:
            for k, v in temp.items():
                d[k] += v
        return d

    def incr(self, d: dict):
        return {(k + 1): v for k, v in d.items()}


if __name__ == '__main__':
    n = NumGoodLeafNodePairs()
    print(n.countPairs(n.form_tree([1, 2, 3, 4, 5, 6, 7]), 3))
