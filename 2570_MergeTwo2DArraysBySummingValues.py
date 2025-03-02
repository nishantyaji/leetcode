# Problem  2570
from typing import List


class MergeTwo2DArraysBySummingValues:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        d = {}
        for k, v in nums1:
            d[k] = v
        for k, v in nums2:
            if k not in d:
                d[k] = v
            else:
                d[k] += v

        return list(map(lambda x: [x[0], x[1]], sorted([(k, v) for k, v in d.items()])))
