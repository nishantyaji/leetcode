# Problem 506

from typing import List


class RelativeRank:
    def findRelativeRanks(self, score: List[int]) -> List[str]:

        str_dict = {1: 'Gold Medal', 2: 'Silver Medal', 3: 'Bronze Medal'}

        def str_val(i: int) -> str:
            if i in str_dict:
                return str_dict[i]
            return str(i)

        my_dict = {}
        nums = list(score)
        nums.sort(reverse=True)
        for idx, n in enumerate(nums):
            my_dict[n] = str_val(idx + 1)

        return [my_dict[i] for i in score]
