# Problem 2050
import functools
from typing import List


class NodeCourse:
    def __init__(self, ordin, val1):
        self.ordinal = ordin
        self.val = val1
        self.children = []
        self.child_set = set()

    def append(self, node):
        if node.ordinal not in self.child_set:
            self.child_set.add(node.ordinal)
            self.children.append(node)


class ParallelCoursesIII:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        node_map = dict()

        prev_nodes, next_nodes = set(), set()
        for relation in relations:
            if relation[0] in node_map:
                node_prev = node_map[relation[0]]
            else:
                node_prev = NodeCourse(relation[0], time[relation[0] - 1])
                node_map[relation[0]] = node_prev

            if relation[1] in node_map:
                node_next = node_map[relation[1]]
            else:
                node_next = NodeCourse(relation[1], time[relation[1] - 1])
                node_map[relation[1]] = node_next

            node_next.append(node_prev)
            prev_nodes.add(relation[0])
            next_nodes.add(relation[1])

        dangling = (set(list(range(1, n+1))) - next_nodes) - prev_nodes
        root_nodes = [node_map[r] for r in list(next_nodes - prev_nodes)]
        return max([self.recurse(root) for root in root_nodes] + [time[i-1] for i in dangling])

    @functools.cache
    def recurse(self, node):
        if node.children is None or len(node.children) == 0:
            return node.val
        return node.val + max([self.recurse(ch) for ch in node.children])


if __name__ == '__main__':
    p = ParallelCoursesIII()
    print(p.minimumTime(3, [[2, 3]], [3, 1, 1]))
    print(p.minimumTime(10, [[3, 9], [9, 10], [3, 10], [9, 1], [9, 5], [10, 5], [3, 5], [1, 6], [3, 6], [5, 6], [9, 6],
                             [10, 6], [1, 7], [3, 7], [5, 7], [6, 7], [9, 7], [10, 7], [10, 4], [1, 8], [2, 8], [3, 8],
                             [4, 8], [6, 8], [7, 8], [9, 8], [10, 8]],
                        [5, 4, 8, 1, 5, 7, 6, 8, 4, 7]))
    print(p.minimumTime(1, [], [1]))
    print(p.minimumTime(3, [[1, 3], [2, 3]], [3, 2, 5]))
    print(p.minimumTime(5, [[1, 5], [2, 5], [3, 5], [3, 4], [4, 5]], [1, 2, 3, 4, 5]))
