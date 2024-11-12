# Problem 2070
from typing import List


class MostBeautifulItemForEachQuery:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        res = [0] * len(queries)
        items += [[x + 1, -i - 1] for i, x in enumerate(queries)]
        items.sort(key=lambda x: (x[0], x[1]))
        max_ = 0
        for [_, beauty] in items:
            if beauty < 0:
                res[-(beauty + 1)] = max_
            else:
                max_ = max(max_, beauty)
        return res

