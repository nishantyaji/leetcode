# Problem 2191
import operator
from typing import List


class SortJumbledNums:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        str_mp = {str(k): str(mapping[k]) for k in mapping}

        def intfy(n: int) -> int:
            return int("".join(list(map(lambda x: str_mp[x], list(str(n))))))

        return list(map(lambda x: x[0], sorted([(x, intfy(x)) for x in nums], key=operator.itemgetter(1))))


if __name__ == '__main__':
    s = SortJumbledNums()
    print(s.sortJumbled([8, 9, 4, 0, 2, 1, 3, 5, 7, 6], [991, 338, 38]))
    print(s.sortJumbled([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [789, 456, 123]))
