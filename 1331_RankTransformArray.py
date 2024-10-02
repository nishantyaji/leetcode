# Problem 1331
from typing import List


class RankTransformArray:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank_dict = {x: (i+1) for i, x in enumerate(sorted(set(arr)))}
        return [rank_dict[x] for x in arr]