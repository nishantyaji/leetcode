# Problem 2657
from typing import List


class FindPrefixCommonArrayOfTwoArrays:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        rev_res = [len(A)]
        a_set, b_set = set(), set()
        for i in range(len(A) - 1):
            if A[-1] in b_set and B[-1] in a_set:
                rev_res.append(rev_res[-1])
            elif A[-1] == B[-1] or B[-1] in a_set or A[-1] in b_set:
                rev_res.append(rev_res[-1] - 1)
            else:
                rev_res.append(rev_res[-1] - 2)
            b_set.add(B.pop())
            a_set.add(A.pop())
        return list(reversed(rev_res))


if __name__ == '__main__':
    f = FindPrefixCommonArrayOfTwoArrays()
    print(f.findThePrefixCommonArray([1, 3, 2, 4], [3, 1, 2, 4]))  # [0,2,3,4]
    print(f.findThePrefixCommonArray([2, 3, 1], [3, 1, 2]))  # [0,1,3]
