# Problem 1971
# Not my own solution.

from typing import List


class FindIfPathExistsInGraph:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        my_set = set()
        my_set.add(source)
        changed_flag = True

        while changed_flag:
            changed_flag = False
            for edge in edges:
                if edge[0] in my_set and edge[1] not in my_set:
                    my_set.add(edge[1])
                    changed_flag = True
                if edge[0] not in my_set and edge[1] in my_set:
                    my_set.add(edge[0])
                    changed_flag = True
                if destination in my_set:
                    return True

        return False


if __name__ == '__main__':
    f = FindIfPathExistsInGraph()
    print(f.validPath(50,
                      [[31, 5], [10, 46], [19, 31], [5, 1], [31, 28], [28, 29], [8, 26], [13, 23], [16, 34], [30, 1],
                       [16, 18], [33, 46], [27, 35], [2, 25], [49, 33], [44, 19], [22, 26], [30, 13], [27, 12], [8, 16],
                       [42, 13], [18, 3], [21, 20], [2, 17], [5, 48], [41, 37], [39, 37], [2, 11], [20, 26], [19, 43],
                       [45, 7], [0, 21], [44, 23], [2, 39], [27, 36], [41, 48], [17, 42], [40, 32], [2, 28], [35, 38],
                       [3, 9], [41, 30], [5, 11], [24, 22], [39, 5], [40, 31], [18, 35], [23, 39], [20, 24], [45, 12]],
                      29, 46))
    print(f.validPath(3, [[0, 1], [1, 2], [2, 0]], 0, 2))
