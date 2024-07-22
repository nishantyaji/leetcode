# Problem 2418
import operator
from typing import List


class SortThePeople:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return list(map(lambda x: x[0], sorted(list(zip(names, heights)), key=operator.itemgetter(1), reverse=True)))
