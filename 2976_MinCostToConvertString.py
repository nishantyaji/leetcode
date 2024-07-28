# Problem 2976
import sys
from typing import List


class MinCostToConvertString:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        dist = [[sys.maxsize for x in range(26)] for y in range(26)]

        def idx(input):
            return ord(input) - ord('a')

        for i in range(26):
            dist[i][i] = 0
        for i in range(len(original)):
            # we do min because there can be many parallel edges from node1 to node2
            # in which case we have to choose the minimum among edges
            dist[idx(original[i])][idx(changed[i])] = min(cost[i], dist[idx(original[i])][idx(changed[i])])

        # Floyd warshall : we calculate the (adj matrix) ** n
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        total_cost = 0
        for i in range(len(source)):
            total_cost += dist[idx(source[i])][idx(target[i])]
        if total_cost >= sys.maxsize:
            return - 1
        return total_cost


if __name__ == '__main__':
    m = MinCostToConvertString()
    print(m.minimumCost("abadcdadac", "baddbccdac", ["d", "c", "d", "c", "b", "a"], ["b", "b", "c", "a", "d", "d"],
                        [8, 5, 9, 1, 10, 2]))
    # 57
    print(m.minimumCost("aabbddccbc", "abbbaabaca", ["a", "b", "c", "b", "a", "d"], ["d", "c", "b", "d", "b", "b"],
                        [3, 8, 7, 6, 7, 10]))
    print(m.minimumCost("aababdbddc", "adcbbbcdba", ["a", "d", "b", "a", "d", "c", "d", "b"],
                        ["b", "a", "d", "c", "c", "a", "b", "a"], [10, 6, 8, 3, 6, 10, 8, 6]))
    #
    print("------")
    print(m.minimumCost("aaadbdcdac", "cdbabaddba", ["a", "c", "b", "d", "b", "a", "c"],
                        ["c", "a", "d", "b", "c", "b", "d"], [7, 2, 1, 3, 6, 1, 7]))
    # 39
    print(m.minimumCost("abcd", "acbe", ["a", "b", "c", "c", "e", "d"], ["b", "c", "b", "e", "b", "e"],
                        [2, 5, 5, 1, 2, 20]))
    # 28
    print(m.minimumCost("aaaa", "bbbb", ["a", "c"], ["c", "b"], [1, 2]))
    # 12
    print(m.minimumCost("abcd", "abce", ["a"], ["e"], [10000]))
    # -1
