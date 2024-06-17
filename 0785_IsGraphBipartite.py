# Problem 785
from typing import List


class IsGraphBartite:

    def isBipartite(self, graph: List[List[int]]) -> bool:
        zeroSet = set()
        withoutZeroSet = set()
        queue = []
        queue.append([True, 0])
        isZeroSet = True

        while True:
            while len(queue) > 0:
                isZeroSet, index = queue[0]
                queue = queue[1:]
                if isZeroSet:
                    if index in withoutZeroSet:
                        return False
                    else:
                        zeroSet.add(index)
                else:
                    if index in zeroSet:
                        return False
                    else:
                        withoutZeroSet.add(index)

                adjacents = graph[index]
                for adj in adjacents:
                    if adj not in zeroSet and adj not in withoutZeroSet:
                        queue.append([not isZeroSet, adj])
            indices = [i for i in range(
                0, len(graph)) if i not in zeroSet and i not in withoutZeroSet]

            if len(indices) == 0:
                break
            else:
                queue.append([isZeroSet, indices[0]])
        return len(zeroSet) + len(withoutZeroSet) == len(graph)


if __name__ == '__main__':
    i = IsGraphBartite()
    print(i.isBipartite([[4], [], [4], [4], [0, 2, 3]]))
    print(i.isBipartite([[], [2, 4, 6], [1, 4, 8, 9], [7, 8], [1, 2, 8, 9], [
          6, 9], [1, 5, 7, 8, 9], [3, 6, 9], [2, 3, 4, 6, 9], [2, 4, 5, 6, 7, 8]]))
    print(i.isBipartite([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]))
    print(i.isBipartite([[1, 3], [0, 2], [1, 3], [0, 2]]))
