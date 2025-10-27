# Problem 2125
import collections
from typing import List


class NumOfLaserBeamsInABank:

    def numberOfBeams(self, bank: List[str]) -> int:

        init, res, prev = False, 0, 0
        for b in bank:
            cntr = collections.Counter(list(b))
            if "1" not in cntr or cntr["1"] == 0:
                continue
            if init:
                res += prev * cntr["1"]
            prev = cntr["1"]
            init = True
        return res
