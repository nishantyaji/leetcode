# Problem 1652
from typing import List


class DefuseTheBomb:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        # this is an unclean and suboptimal code
        # O(n) is the complexity that I need to code
        # and write a common logic for both +ve and -ve k
        # I'll do that some other day when time permits
        # Right now, committing the code that I cobbled together in a jiffy
        if k == 0:
            return [0] * len(code)
        res = []
        j = 1 if (k > 0) else -1
        if j > 0:
            code_repeat = code + code
            for i in range(len(code)):
                res.append(sum(code_repeat[i + j:i + k + j]))
        else:
            code_repeat = code + code + code
            for i in range(len(code) * 2, len(code), -1):
                res.append(sum(code_repeat[i + k + j:i + j]))
            res.reverse()
        return res