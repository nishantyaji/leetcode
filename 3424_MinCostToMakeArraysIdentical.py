# Problem 3424
from typing import List


class MinCostToMakeArraysIdentical:

    def minCost(self, arr: List[int], brr: List[int], k: int) -> int:
        init_cost = 0
        for i in range(len(arr)):
            init_cost += abs(arr[i] - brr[i])
        arr_tuples = [(x, i) for i, x in enumerate(arr)]
        brr_tuples = [(x, i) for i, x in enumerate(brr)]
        arr_tuples.sort(key=lambda x: x[0])
        brr_tuples.sort(key=lambda x: x[0])
        cost = 0
        for i in range(len(arr)):
            if arr_tuples[i][1] != brr_tuples[i][1]:
                cost += k
                break
        for i in range(len(arr)):
            cost += abs(arr_tuples[i][0] - brr_tuples[i][0])
        return min(init_cost, cost)
