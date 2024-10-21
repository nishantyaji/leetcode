# Problem 765
import collections
import copy
import functools
import sys
from typing import List


class CouplesHoldingHands:
    """
    look at this short solution:
    https://leetcode.com/problems/couples-holding-hands/solutions/2175649/python-6-lines-greedy-t-s-96-98/
    """
    def minSwapsCouples(self, row: List[int]) -> int:
        sep = "_"
        row = [(r // 2) for r in row]
        row_str = sep.join(map(str, row))
        return self.recur(row_str, sep)

    @functools.cache
    def recur(self, row_str: str, sep: str) -> int:
        if len(row_str.strip()) == 0:
            return 0
        row = list(map(int, row_str.split(sep)))
        num_couples = len(row) // 2
        group = collections.defaultdict(set)
        inv_group = collections.defaultdict(set)
        ordered = set(row)

        modified = False
        for i in range(0, num_couples):
            if row[2 * i] == row[2 * i + 1]:
                ordered.remove(row[2 * i])
                modified = True
            else:
                group[i].add(row[2 * i])
                group[i].add(row[2 * i + 1])
                inv_group[row[2 * i + 1]].add(i)
                inv_group[row[2 * i]].add(i)

        keys = group.keys()
        num_swaps = 0
        for i in range(len(keys)):
            for j in range(i + 1, len(keys)):
                if group[i] == group[j] and group[i]:
                    modified = True
                    # 1 swap will pair 2 couples
                    num_swaps += 1
                    for elem in list(group[i]):
                        ordered.remove(elem)

        min_swap = sys.maxsize
        if not modified:
            for o in ordered:
                a, b = min(inv_group[o]), max(inv_group[o])
                not_o = 2 * a + 1 if row[2 * a] == o else 2 * a
                b_ = 2 * b if row[2 * b] == o else 2 * b + 1
                # swap
                row_copy = copy.deepcopy(row)
                temp = row_copy[not_o]
                row_copy[not_o] = row_copy[b_]
                row_copy[b_] = temp
                # end swap
                ordered_copy = copy.deepcopy(ordered)
                ordered_copy.remove(o)
                # Add 1 for the swap above
                this_swap = 1 + self.recur(self.get_new_row_str(ordered_copy, row_copy, sep), sep)
                min_swap = min(min_swap, this_swap)
                return min_swap
        else:
            return num_swaps + self.recur(self.get_new_row_str(ordered, row, sep), sep)

    def get_new_row_str(self, st: set, old: List[int], sep: str) -> str:
        mp = {x: i for i, x in enumerate(sorted(st))}
        return sep.join(list(map(str, [mp[x] for x in old if x in mp])))


if __name__ == '__main__':
    c = CouplesHoldingHands()
    print(c.minSwapsCouples([16, 5, 17, 11, 2, 3, 14, 8, 12, 13, 6, 0, 15, 7, 1, 9, 10, 4]))  # 5
    print(c.minSwapsCouples([5, 4, 2, 6, 3, 1, 0, 7]))  # 2
    print(c.minSwapsCouples([0, 2, 1, 3]))  # 1
    print(c.minSwapsCouples([3, 2, 0, 1]))  # 0
