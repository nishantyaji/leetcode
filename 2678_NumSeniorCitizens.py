# Problem 2678
from typing import List


class NumSeniorCitizens:
    def countSeniors(self, details: List[str]) -> int:
        return len(list(filter(lambda x: x > 60, map(lambda x: int(x[11:13]), details))))
