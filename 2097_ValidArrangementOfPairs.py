# Problem 2097
import collections
import copy
import itertools
from typing import List


class ValidArrangementOfPairs:

    # Hierholzer algorithm (GFG)
    def get_circuit(self, adj, start):
        if len(adj) == 0:
            return
        curr_path = [start]
        circuit = []

        while curr_path:
            curr_v = curr_path[-1]
            if curr_v in adj and adj[curr_v]:
                next_v = adj[curr_v].pop()
                curr_path.append(next_v)
            else:
                circuit.append(curr_path.pop())

        return circuit

    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:

        cntr = collections.Counter(list(itertools.chain(*pairs)))
        odd_nums = set([k for k, v in cntr.items() if v % 2 == 1])
        start_cntr = collections.Counter(list(map(lambda x: x[0], pairs)))
        end_cntr = collections.Counter(list(map(lambda x: x[1], pairs)))
        start, end = (max(cntr.keys()), max(cntr.keys()))
        if odd_nums:
            for k in odd_nums:
                if start_cntr[k] < end_cntr[k]:
                    end = k
                elif start_cntr[k] > end_cntr[k]:
                    start = k

        adj = {}
        for i in range(len(pairs)):
            if pairs[i][1] not in adj:
                adj[pairs[i][1]] = list()
            adj[pairs[i][1]].append(pairs[i][0])

        circuit = self.get_circuit(adj, end)
        res = [[circuit[i], circuit[i+1]] for i in range(len(circuit) - 1)]
        print(res)
        return res



if __name__ == '__main__':
    v = ValidArrangementOfPairs()
    print(v.validArrangement([[5,13],[10,6],[11,3],[15,19],[16,19],[1,10],[19,11],[4,16],[19,9],[5,11],[5,6],[13,5],[13,9],[9,15],[11,16],[6,9],[9,13],[3,1],[16,5],[6,5]]))
    print(v.validArrangement(
        [[0, 8], [11, 20], [4, 15], [18, 17], [17, 4], [6, 14], [15, 0], [13, 3], [14, 9], [19, 13], [3, 11], [2, 19],
         [20, 2], [9, 19], [8, 6]]))
    print(v.validArrangement([[1, 2], [1, 3], [2, 1]]))
    print(v.validArrangement([[8, 5], [8, 7], [0, 8], [0, 5], [7, 0], [5, 0], [0, 7], [8, 0], [7, 8]]))
    print(v.validArrangement([[17, 18], [18, 10], [10, 18]]))
    print(v.validArrangement([[1, 3], [3, 2], [2, 1]]))
    print(v.validArrangement([[5, 1], [4, 5], [11, 9], [9, 4]]))
